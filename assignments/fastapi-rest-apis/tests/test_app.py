import importlib.util
import pathlib

from fastapi.testclient import TestClient

# Load the src/app.py module directly to avoid package import issues
ROOT = pathlib.Path(__file__).resolve().parents[1]
APP_PATH = ROOT / "src" / "app.py"
spec = importlib.util.spec_from_file_location("app_module", APP_PATH)
app_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app_module)


client = TestClient(app_module.app)


def test_read_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "FastAPI is up"}


def test_get_existing_item():
    r = client.get("/items/1")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == 1
    assert "name" in data


def test_create_item_and_invalid():
    # valid create
    payload = {"name": "New Item", "description": "Created by test"}
    r = client.post("/items", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data["name"] == payload["name"]

    # invalid payload (missing name)
    r2 = client.post("/items", json={"description": "no name"})
    assert r2.status_code == 422
