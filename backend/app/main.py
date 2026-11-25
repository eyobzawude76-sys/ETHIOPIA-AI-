"""ETHIOPIA AI backend API.

The chat endpoint intentionally reports that no model is configured yet.
A model runtime will be selected after checking the target Android device.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="ETHIOPIA AI API",
    description="Early API foundation for Afaan Oromoo and Afaan Amharic AI assistance.",
    version="0.1.0",
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
def chat(request: ChatRequest) -> ChatResponse:
    """Placeholder until an open-source model runtime is integrated."""
    if not request.message.strip():
        raise HTTPException(status_code=422, detail="Message cannot be blank.")
    raise HTTPException(
        status_code=501,
        detail=(
            "AI model is not connected yet. The model will be selected "
            "after checking the Android device's RAM and storage."
        ),
    )
