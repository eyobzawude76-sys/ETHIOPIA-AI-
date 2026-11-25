# ETHIOPIA AI Backend

This is the first API skeleton. It does **not** generate AI answers yet; the open-source model runtime has not been selected or connected.

## Run locally

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
uvicorn app.main:app --app-dir backend --reload
```

Open the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Endpoints

- `GET /health` — confirms that the API process is running.
- `POST /api/v1/chat` — defined request contract; returns HTTP 501 until a model runtime is integrated.

## Tests

Install the test dependencies and run:

```bash
pip install pytest httpx
PYTHONPATH=backend pytest backend/tests
```

## Next step

Check the Android device's RAM, free storage, and Android version before choosing an appropriately sized GGUF model and inference runtime.
