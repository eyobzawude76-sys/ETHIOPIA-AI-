"""ETHIOPIA AI backend API."""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.model_client import (
    ModelNotConfiguredError,
    ModelUpstreamError,
    generate_reply,
)

app = FastAPI(
    title="ETHIOPIA AI API",
    description="AI assistant API for Afaan Oromoo and Afaan Amharic.",
    version="0.2.0",
)


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)
    language: str = Field(default="auto", pattern="^(auto|om|am)$")


class ChatResponse(BaseModel):
    status: str
    message: str


@app.get("/health")
def health() -> dict[str, str]:
    """Report whether the API process is running."""
    return {"status": "ok", "project": "ETHIOPIA AI"}


@app.post("/api/v1/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    """Send a user message to the configured OpenAI-compatible model server."""
    if not request.message.strip():
        raise HTTPException(status_code=422, detail="Message cannot be blank.")
    try:
        answer = await generate_reply(request.message.strip(), request.language)
        return ChatResponse(status="ok", message=answer)
    except ModelNotConfiguredError as exc:
        raise HTTPException(
            status_code=503,
            detail="AI model is not configured. Set MODEL_BASE_URL on the backend.",
        ) from exc
    except ModelUpstreamError as exc:
        raise HTTPException(
            status_code=502,
            detail="The AI model server could not complete the request.",
        ) from exc
