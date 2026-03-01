from ag_ui_adk import add_adk_fastapi_endpoint
from dotenv import load_dotenv
from fastapi import FastAPI

from agents.hello import adk_hello_agent

load_dotenv()


app = FastAPI(title="ADK Middleware Proverbs Agent")

add_adk_fastapi_endpoint(app, adk_hello_agent, path="/")

if __name__ == "__main__":
    import os

    import uvicorn

    if not os.getenv("GOOGLE_API_KEY"):
        print("⚠️  Warning: GOOGLE_API_KEY environment variable not set!")
        print("   Set it with: export GOOGLE_API_KEY='your-key-here'")
        print("   Get a key from: https://makersuite.google.com/app/apikey")
        print()

    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
