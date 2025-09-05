import asyncio
import os
from pathlib import Path
from fastapi import FastAPI, Form
from fastapi.responses import StreamingResponse
from mangum import Mangum

# Load environment variables
env_vars = {
    'OPENAI_API_KEY': os.environ.get('OPENAI_API_KEY', ''),
    'LANGCHAIN_API_KEY': os.environ.get('LANGCHAIN_API_KEY', ''),
    'SERPAPI_API_KEY': os.environ.get('SERPAPI_API_KEY', '')
}

for key, value in env_vars.items():
    if value:
        os.environ[key] = value

# Import after setting environment variables
import sys
sys.path.append(str(Path(__file__).parent.parent.parent / 'chapters' / '09-capstone' / 'api'))

from agent import QueueCallbackHandler, agent_executor

app = FastAPI()

# streaming function
async def token_generator(content: str, streamer: QueueCallbackHandler):
    task = asyncio.create_task(agent_executor.invoke(
        input=content,
        streamer=streamer,
        verbose=True
    ))
    
    async for token in streamer:
        try:
            if token == "<<STEP_END>>":
                yield "</step>"
            elif tool_calls := token.message.additional_kwargs.get("tool_calls"):
                if tool_name := tool_calls[0]["function"]["name"]:
                    yield f"<step><step_name>{tool_name}</step_name>"
                if tool_args := tool_calls[0]["function"]["arguments"]:
                    yield tool_args
        except Exception as e:
            print(f"Error streaming token: {e}")
            continue
    await task

@app.post("/invoke")
async def invoke(content: str = Form()):
    queue: asyncio.Queue = asyncio.Queue()
    streamer = QueueCallbackHandler(queue)
    
    return StreamingResponse(
        token_generator(content, streamer),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    )

# Mangum handler for Vercel
handler = Mangum(app)
