import os
from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Simple FastAPI app for debugging
app = FastAPI(title="LangChain Debug API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://lang-chain-course.vercel.app",
        "https://*.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"status": "API is running", "message": "LangChain Debug API"}

@app.get("/health")
async def health_check():
    """Detailed health check with environment variables"""
    env_status = {
        "OPENAI_API_KEY": "✅ Set" if os.environ.get("OPENAI_API_KEY") else "❌ Missing",
        "SERPAPI_API_KEY": "✅ Set" if os.environ.get("SERPAPI_API_KEY") else "❌ Missing",
        "LANGCHAIN_API_KEY": "✅ Set" if os.environ.get("LANGCHAIN_API_KEY") else "❌ Missing",
    }
    
    return {
        "status": "healthy",
        "environment_variables": env_status,
        "python_version": os.sys.version,
        "available_env_vars": [key for key in os.environ.keys() if "API" in key.upper() or "KEY" in key.upper()]
    }

@app.post("/invoke")
async def invoke_simple(content: str = Form()):
    """Simplified invoke endpoint for testing"""
    
    # Check if required environment variables are available
    if not os.environ.get("OPENAI_API_KEY"):
        return JSONResponse(
            status_code=500,
            content={"error": "OPENAI_API_KEY not configured"}
        )
    
    # For now, return a simple response without calling the actual agent
    return JSONResponse(content={
        "message": f"Received: {content}",
        "status": "success",
        "note": "This is a simplified response for testing. Full agent functionality will be restored once environment is working."
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
