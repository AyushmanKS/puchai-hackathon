# from fastapi import FastAPI, Request
# from pydantic import BaseModel, Field
# from typing import Annotated

# # Import the get_news function we already created and tested
# from news_fetcher import get_news

# # Initialize our FastAPI application
# app = FastAPI(
#     title="Personalized News Aggregator",
#     description="An MCP server that provides personalized news articles as a tool for an AI assistant.",
# )

# # --- Tool Definition ---
# class NewsRequest(BaseModel):
#     topic: Annotated[str, Field(description="The topic the user is interested in.")]

# @app.post("/get_personalized_news")
# async def get_personalized_news_endpoint(request: NewsRequest) -> dict:
#     print(f"Received request for news on topic: {request.topic}")
#     articles = get_news(request.topic)
#     news_summary = "\n".join(articles)
#     return {"content": f"Here are the latest articles about {request.topic}:\n{news_summary}"}


# # --- MCP Manifest ---
# # The endpoint that tells PuchAI what our server is and what tools it offers.
# # We now accept BOTH GET and POST requests for maximum compatibility.

# @app.get("/mcp")
# @app.post("/mcp") # <<< THIS IS THE NEW LINE YOU ARE ADDING
# def mcp_manifest():
#     """
#     Provides the manifest that describes the server's tools to PuchAI.
#     """
#     return {
#         "name": "Personalized News Aggregator",
#         "description": "Fetches personalized news articles for users.",
#         "tools": {
#             "news": {
#                 "description": "Get the latest news about a specific topic.",
#                 "use_when": "The user specifically asks for a 'news report' or 'news summary' on a topic.",
#                 "endpoint": "/get_personalized_news",
#                 "parameters": {
#                     "topic": {
#                         "type": "string",
#                         "description": "The subject or topic of interest for news articles.",
#                         "required": True
#                     }
#                 }
#             }
#         }
#     }

# # A simple root endpoint to easily check if the server is running
# @app.get("/")
# def read_root():
#     return {"message": "Personalized News Aggregator MCP Server is running."}

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated

# We are not even importing the news_fetcher for this test
# from news_fetcher import get_news

app = FastAPI(
    title="MCP Test Server",
    description="A server for testing a basic, instant tool.",
)

# --- NEW Hello World Tool Definition ---
@app.post("/hello_world")
async def hello_world_endpoint() -> dict:
    """
    An instant tool that just says hello. It does no work.
    """
    print("Received request for the hello_world tool!") # A new print statement!
    return {"content": "Hello from my custom tool! The connection is working!"}


# --- MCP Manifest ---
# We have updated the manifest to only show the new tool.
@app.get("/mcp")
@app.post("/mcp")
def mcp_manifest():
    return {
        "name": "Connection Test Server",
        "description": "A server to test a basic tool connection.",
        "tools": {
            "hello": { # Changed tool name to "hello"
                "description": "A simple test tool that says hello.",
                "use_when": "The user asks to say hello or run the connection test.",
                "endpoint": "/hello_world", # Point to the new endpoint
                "parameters": {} # No parameters needed
            }
        }
    }

@app.get("/")
def read_root():
    return {"message": "Test MCP Server is running."}