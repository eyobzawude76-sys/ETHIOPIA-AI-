"""OpenAI-compatible remote model client for ETHIOPIA AI.

Configure MODEL_BASE_URL and MODEL_NAME in the backend environment.
The endpoint can be provided by llama.cpp, vLLM, or another compatible server.
"""
import os

import httpx


class ModelNotConfiguredError(RuntimeError):
    """Raised when no model endpoint has been configured."""


class ModelUpstreamError(RuntimeError):
    """Raised when the configured model server cannot answer."""


async def generate_reply(message: str, language: str = "auto") -> str:
    base_url = os.getenv("MODEL_BASE_URL", "").strip().rstrip("/")
    model_name = os.getenv("MODEL_NAME", "local-model").strip()
    api_key = os.getenv("MODEL_API_KEY", "").strip()

    if not base_url:
        raise ModelNotConfiguredError("MODEL_BASE_URL is not configured.")

    language_instruction = {
        "om": "Reply in Afaan Oromoo.",
        "am": "Reply in Afaan Amharic (አማርኛ).",
        "auto": "Reply in the language used by the user. Support Afaan Oromoo and Afaan Amharic.",
    }[language]

    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    payload = {
        "model": model_name,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are ETHIOPIA AI, a helpful assistant. "
                    + language_instruction
                    + " If you are unsure, say so rather than inventing facts."
                ),
            },
            {"role": "user", "content": message},
        ],
        "temperature": 0.7,
    }

    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                f"{base_url}/chat/completions",
                headers=headers,
                json=payload,
            )
            response.raise_for_status()
            data = response.json()
            answer = data["choices"][0]["message"]["content"]
            if not isinstance(answer, str) or not answer.strip():
                raise ModelUpstreamError("Model server returned an empty response.")
            return answer.strip()
    except ModelUpstreamError:
        raise
    except (httpx.HTTPError, KeyError, IndexError, TypeError, ValueError) as exc:
        raise ModelUpstreamError("The model server request failed.") from exc
