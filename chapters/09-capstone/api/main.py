import asyncio
import os
from pathlib import Path

# Load environment variables - works for both local development and production
env_file = Path(__file__).parent.parent.parent.parent / '.env'
if env_file.exists():
    # Local development - load from .env file
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if '=' in line and not line.startswith('#') and line:
                key, value = line.split('=', 1)
                os.environ[key] = value

# Verify required environment variables
required_vars = ["OPENAI_API_KEY", "SERPAPI_API_KEY"]
missing_vars = [var for var in required_vars if not os.environ.get(var)]

if missing_vars:
    print(f"ERROR: Missing environment variables: {missing_vars}")
    raise RuntimeError(f"Missing required environment variables: {missing_vars}")

try:
    from agent import QueueCallbackHandler, agent_executor
    AGENT_AVAILABLE = True
    print("✅ Agent imported successfully")
except Exception as e:
    print(f"⚠️ Agent import failed: {e}")
    AGENT_AVAILABLE = False

from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI(title="LangChain Agent API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Local development
        "https://lang-chain-course.vercel.app",  # Production frontend
        "https://*.vercel.app",  # Any Vercel deployment
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "LangChain Agent API is running",
        "agent_available": AGENT_AVAILABLE,
        "version": "1.0.0"
    }

# streaming function
async def token_generator(content: str, streamer: QueueCallbackHandler):
    if not AGENT_AVAILABLE:
        yield "Agent is not available due to import errors. Please check logs."
        return
        
    task = asyncio.create_task(agent_executor.invoke(
        input=content,
        streamer=streamer,
        verbose=True  # set to True to see verbose output in console
    ))
    # initialize various components to stream
    async for token in streamer:
        try:
            if token == "<<STEP_END>>":
                # send end of step token
                yield "</step>"
            elif tool_calls := token.message.additional_kwargs.get("tool_calls"):
                if tool_name := tool_calls[0]["function"]["name"]:
                    # send start of step token followed by step name tokens
                    yield f"<step><step_name>{tool_name}</step_name>"
                if tool_args := tool_calls[0]["function"]["arguments"]:
                    # tool args are streamed directly, ensure it's properly encoded
                    yield tool_args
        except Exception as e:
            print(f"Error streaming token: {e}")
            continue
    await task

# invoke function
@app.post("/invoke")
async def invoke(content: str = Form()):
    if not AGENT_AVAILABLE:
        return JSONResponse(
            status_code=503,
            content={
                "error": "Agent is not available", 
                "message": "There was an error loading the LangChain agent. Please check the server logs."
            }
        )
    
    try:
        queue: asyncio.Queue = asyncio.Queue()
        streamer = QueueCallbackHandler(queue)
        # return the streaming response
        return StreamingResponse(
            token_generator(content, streamer),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
            }
        )
    except Exception as e:
        print(f"Error in invoke endpoint: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.get("/health")
async def health_check():
    """Detailed health check"""
    env_status = {
        "OPENAI_API_KEY": "✅ Set" if os.environ.get("OPENAI_API_KEY") else "❌ Missing",
        "SERPAPI_API_KEY": "✅ Set" if os.environ.get("SERPAPI_API_KEY") else "❌ Missing", 
        "LANGCHAIN_API_KEY": "✅ Set" if os.environ.get("LANGCHAIN_API_KEY") else "❌ Missing",
    }
    
    return {
        "status": "healthy",
        "agent_available": AGENT_AVAILABLE,
        "environment_variables": env_status,
        "python_version": os.sys.version,
    }
