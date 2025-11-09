"""Starter code example: minimal FastAPI app entrypoint.

This file is a tiny example and can be copied to `src/app.py` or used as a reference.
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "FastAPI starter is running"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"id": item_id, "name": f"Item {item_id}"}
