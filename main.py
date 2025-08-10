# ==============================================================================
# main.py - Fake News Verifier MCP Server for PuchAI Hackathon
#
# Author: [Your Name/Team Name]
# Date: August 10, 2025
#
# Description:
# This FastAPI server acts as a Model-Context-Protocol (MCP) provider for the
# PuchAI assistant. It exposes a custom tool that allows users to submit a
# news headline or claim and receive a verification analysis.
#
# For the purpose of this hackathon demo, the verification logic is mocked
# to ensure a fast, reliable, and consistent user experience, bypassing
# potential latencies from live fact-checking APIs.
# ==============================================================================

# --- Core Dependencies ---
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated

# --- Application Initialization ---
# Instantiate the FastAPI application. The title and description are used for
# auto-generated API documentation (e.g., at the /docs endpoint).
app = FastAPI(
    title="Fake News Verifier",
    description="An MCP server that helps users fact-check news headlines.",
)


# --- Mocked Verification Logic ---
# In a production environment, this function would connect to a live fact-checking
# API or a database of known misinformation. For this demo, we use a mocked
# response to guarantee instant performance and reliability.
def verify_claim_mocked(claim: str) -> str:
    """
    Simulates the verification of a news claim and returns a formatted analysis.

    Args:
        claim (str): The suspicious headline or claim from the user.

    Returns:
        str: A formatted string containing the mock verification results.
    """
    print(f"Verification request received for claim: '{claim}'. Returning mocked response.")
    
    # This response template can be customized to be more dynamic or detailed.
    response_template = f"""
Regarding the claim: "{claim}"

Our analysis suggests the following:
- **Credibility Score:** Low
- **Source Analysis:** We could not find this claim reported by major, reputable news outlets (like BBC, Reuters, Associated Press).
- **Recommendation:** This claim has the characteristics of misinformation. Please be cautious and avoid sharing it until it is confirmed by trusted sources.
"""
    return response_template


# --- PuchAI Integration Endpoints ---

# The '/validate' endpoint is a mandatory security requirement from PuchAI.
# It is called upon connection to verify that the user connecting the server
# is the legitimate owner.
@app.post("/validate")
async def validate_endpoint() -> dict:
    """
    Handles the validation request from PuchAI by returning a hardcoded phone number.
    
    Note: In this demo version, the number is hardcoded for simplicity. In a
    production server, this would be loaded securely from an environment variable.
    """
    my_number = "917755087157" # This must match the user's registered PuchAI number.
    print(f"Validation request received. Returning hardcoded number: {my_number}")
    return {"content": my_number}


# Pydantic model for request body validation.
# This ensures that any request to our '/verify_news' endpoint contains a 'claim' field.
class VerifyRequest(BaseModel):
    claim: Annotated[str, Field(description="The headline or claim the user wants to fact-check.")]


# This is the primary tool endpoint for our application.
@app.post("/verify_news")
async def verify_news_endpoint(request: VerifyRequest) -> dict:
    """
    Receives a claim from PuchAI, processes it using our verification logic,
    and returns the analysis.
    """
    analysis = verify_claim_mocked(request.claim)
    # The response must be a JSON object with a "content" key.
    return {"content": analysis}


# The '/mcp' endpoint is the manifest that describes the server's capabilities to PuchAI.
# It acts as a "menu" that the AI reads to learn what tools are available.
@app.get("/mcp")
@app.post("/mcp")
def mcp_manifest():
    """
    Provides the MCP manifest.

    This JSON object defines the server's identity and lists all available tools,
    including their purpose, endpoint, and expected parameters. The 'use_when'
    field is crucial, as it provides a natural language hint to the AI about
    when to use a specific tool.
    """
    return {
        "name": "Fake News Verifier",
        "description": "A tool to help users fact-check and verify news claims.",
        "tools": {
            # The mandatory 'validate' tool for security.
            "validate": {
                "description": "Validates server ownership.",
                "endpoint": "/validate",
                "parameters": {}
            },
            # Our custom 'verify' tool.
            "verify": {
                "description": "Fact-checks a news headline or a claim.",
                "use_when": "The user wants to verify, fact-check, or know if a piece of news is fake or real.",
                "endpoint": "/verify_news",
                "parameters": {
                    "claim": {
                        "type": "string",
                        "description": "The suspicious news headline or claim to be verified.",
                        "required": True
                    }
                }
            }
        }
    }
