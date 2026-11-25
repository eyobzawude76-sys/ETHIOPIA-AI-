import pytest

from app.model_client import ModelNotConfiguredError, generate_reply


@pytest.mark.asyncio
async def test_model_client_requires_base_url(monkeypatch):
    monkeypatch.delenv("MODEL_BASE_URL", raising=False)
    monkeypatch.setenv("MODEL_NAME", "test-model")

    with pytest.raises(ModelNotConfiguredError):
        await generate_reply("Akkam jirta?", "om")
