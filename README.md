# Fake News Verifier - PuchAI Hackathon Submission

**Team Name:** [Your Team Name or Your Name]

---

## 🚀 The Problem

In the age of social media, misinformation and "fake news" spread like wildfire on platforms like WhatsApp, causing confusion and harm. It is increasingly difficult for the average user to distinguish between credible information and fabricated claims.

## ✨ Our Solution

The **Fake News Verifier** is an AI-powered tool built for the PuchAI assistant that provides users with an instant first-pass analysis of suspicious news headlines or claims. By simply asking the AI to verify a claim, users can get an immediate credibility assessment, helping to curb the spread of fake news directly within their messaging app.

---

## Demo

**Live Deployed Link:** `[You will get this link after deploying to Render]`

### How to Use

1.  Connect our MCP server to your PuchAI assistant using the live link above.
2.  Send a message to the AI asking it to verify a claim. For example:
    - *"Verify if the claim that scientists have discovered dragons is real."*
    - *"Is this news true: the government is giving everyone free laptops?"*

---

## 🛠️ Technical Details

- **Language:** Python
- **Framework:** FastAPI
- **Protocol:** PuchAI Model-Context-Protocol (MCP)
- **Deployment:** Render.com

**Note on Demonstration:** For the purpose of this hackathon demo, the verification logic is **mocked**. This design choice guarantees a fast, reliable, and consistent user experience, bypassing potential latencies and rate limits from live fact-checking APIs. This allows us to prove that the core logic—connecting to PuchAI, understanding user intent, and returning a formatted response—is working perfectly.
