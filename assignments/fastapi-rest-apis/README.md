# 📘 Assignment: Building REST APIs with FastAPI

---
slug: fastapi-rest-apis
id: fastapi-rest-apis
difficulty: Intermediate
estimated_time: 90–150 minutes
prerequisites:
  - Python 3.9+
  - Basic knowledge of HTTP, JSON and Python
  - Familiarity with virtual environments and pytest
due_date: 2025-11-16
attachments:
  - name: Starter Code
    file: starter-code.py
    type: python
---

Short description: Build a small RESTful API using FastAPI. Implement several endpoints, validation with Pydantic models, and write tests using FastAPI's TestClient.

## 🎯 Objective
Learn how to design and implement REST endpoints with FastAPI, validate input with Pydantic, and write tests for API behavior.

## 🎓 Learning Goals
After completing this assignment, students will be able to:
- Create a FastAPI application with multiple endpoints
- Use Pydantic models for request/response validation
- Write tests using FastAPI's TestClient (pytest)
- Run and serve the application with Uvicorn

## ℹ️ Information
- Difficulty: Intermediate
- Estimated Time: 90–150 minutes
- Prerequisites: Python 3.9+, basic HTTP and JSON knowledge
- Submission Format: folder `assignments/fastapi-rest-apis/` as described below

## 📝 Tasks (steps and requirements)

### 🛠️ Task 1 — Implement API core
#### Description
Implement a small REST API for managing "items" (CRUD-like minimal). Focus on clear request/response models and testable handlers.

#### Steps
1. Create/verify folder `assignments/fastapi-rest-apis/`
2. Implement `assignments/fastapi-rest-apis/src/app.py` with at least:
   - GET `/` — health/message
   - GET `/items/{item_id}` — get item by id
   - POST `/items` — create an item (accepts Pydantic model)
3. Add `assignments/fastapi-rest-apis/src/main.py` as a simple entry point using Uvicorn
4. Add automated tests in `assignments/fastapi-rest-apis/tests/test_app.py`
5. Add `requirements.txt` listing dependencies

#### Acceptance Criteria
- Endpoints return correct status codes and JSON shapes
- Input validated by Pydantic models; invalid input returns 422
- Tests cover happy path and at least one error case
- Application can be started with Uvicorn

#### Files to change / create
- `assignments/fastapi-rest-apis/README.md` — this file
- `assignments/fastapi-rest-apis/starter-code.py` — minimal starter example
- `assignments/fastapi-rest-apis/src/app.py` — main FastAPI app
- `assignments/fastapi-rest-apis/src/main.py` — uvicorn entrypoint
- `assignments/fastapi-rest-apis/tests/test_app.py` — pytest tests
- `assignments/fastapi-rest-apis/requirements.txt` — dependencies

#### Tips
- Keep logic small and testable; avoid global side-effects that break tests
- Use explicit response models for clarity

---

## ✅ Evaluation Criteria (example)
- Functionality: 60%
- Code and style: 20%
- Documentation (README): 10%
- Tests/coverage: 10%

## 💾 Run and Test Locally
Commands for Debian GNU/Linux 13 (devcontainer):

```bash
# Create and activate a virtual environment (optional but recommended)
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip3 install -r assignments/fastapi-rest-apis/requirements.txt

# Run the app (development)
cd assignments/fastapi-rest-apis
python3 src/main.py

# Run tests
pytest -q
```

## 📎 Submission structure
- `README.md` — instructions and description (this file)
- `src/` — source code
- `tests/` — pytest tests
- `starter-code.py` — starter example (optional to use)

---

If you want, I can also add a small exercise extension (auth, pagination, file-backed storage) as Task 2.
