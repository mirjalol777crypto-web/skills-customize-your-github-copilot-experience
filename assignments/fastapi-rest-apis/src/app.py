from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None


# In-memory store for demonstration and tests
_items: dict[int, dict] = {1: {"id": 1, "name": "Sample Item", "description": "A sample."}}


@app.get("/")
def read_root():
    return {"message": "FastAPI is up"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = _items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", status_code=201)
def create_item(item: Item):
    new_id = max(_items.keys()) + 1 if _items else 1
    _items[new_id] = {"id": new_id, "name": item.name, "description": item.description}
    return _items[new_id]
