from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import os
import logging
from llama_cpp import Llama

# Initialize FastAPI app
app = FastAPI(title="GenZ Model Runner", 
             description="Local AI model execution service for Bangla AGI models")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "http://model-runner.docker.internal/engines/llama.cpp/v1/")
DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "index.docker.io/ai/qwen2.5:7B-F16")

# Initialize model
try:
    model = Llama(model_path=DEFAULT_MODEL, 
                 n_ctx=8192,  # Support long contexts
                 n_gpu_layers=-1)  # Use all available GPU layers
    logger.info(f"Model {DEFAULT_MODEL} loaded successfully")
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    model = None

class CompletionRequest(BaseModel):
    prompt: str
    max_tokens: Optional[int] = 100
    temperature: Optional[float] = 0.7
    stream: Optional[bool] = False

# Health check endpoint
@app.get("/health")
async def health_check():
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    return {"status": "healthy", "model": DEFAULT_MODEL}

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "GenZ Model Runner API",
        "model": DEFAULT_MODEL,
        "endpoints": {
            "/health": "Health check endpoint",
            "/v1/completions": "Get model completions",
            "/v1/chat": "Chat with the model"
        }
    }

# Completions endpoint
@app.post("/v1/completions")
async def get_completion(request: CompletionRequest):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        response = model(
            request.prompt,
            max_tokens=request.max_tokens,
            temperature=request.temperature,
            stream=request.stream
        )
        return {"completion": response["choices"][0]["text"]}
    except Exception as e:
        logger.error(f"Completion error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
