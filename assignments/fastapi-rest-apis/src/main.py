"""Simple uvicorn entrypoint for the FastAPI app in `src/app.py`.

Run this file to start the development server:
    python3 src/main.py
"""
import uvicorn


if __name__ == "__main__":
    uvicorn.run("src.app:app", host="127.0.0.1", port=8000, log_level="info")
