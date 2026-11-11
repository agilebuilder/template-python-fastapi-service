# AGENTS.md — Navigation Guide for AI Coding Agents

<% var pkg = packageDir.charAt(0) === '<' ? snakeCase(projectName) : packageDir -%>
This project is an async API service built on FastAPI + SQLAlchemy 2.x (asyncio) + Pydantic v2 with a src layout.

## Project Structure

- `src/<%= pkg %>/main.py`: application entry. The `create_app()` factory builds the FastAPI instance and auto-creates tables in lifespan; `main()` starts uvicorn.
- `src/<%= pkg %>/api/router.py`: router aggregation. After adding a new route module under `api/routes/`, include it here with `include_router`.
- `src/<%= pkg %>/api/routes/`: HTTP routing layer. Only parse parameters, call services, and return responses — no business logic here.
- `src/<%= pkg %>/core/config.py`: `Settings` (pydantic-settings). Read all configuration from here; do not scatter raw environment variable reads.
- `src/<%= pkg %>/db/session.py`: async engine and `async_session_factory`; `get_session` is a FastAPI dependency — routes obtain sessions via `Depends(get_session)`.
- `src/<%= pkg %>/models/`: SQLAlchemy ORM models; all inherit `Base` from `models/base.py`.
- `src/<%= pkg %>/schemas/`: Pydantic v2 request/response models, kept separate from ORM models.
- `src/<%= pkg %>/services/`: business logic and database operations; routes and sessions meet here.
- `tests/`: pytest tests. `conftest.py` overrides the `get_session` dependency with in-memory SQLite; the `client` fixture provides an httpx AsyncClient.

## Conventions

- Use relative imports inside the package (e.g. `from ..core.config import settings`); use absolute imports `<%= pkg %>.xxx` outside the package (tests).
- Full async stack: routes, services, and DB operations are all `async def` — do not mix in sync SQLAlchemy calls.
- Type-annotate all code; new ORM models must be exported in `models/__init__.py` so metadata is complete at table creation.
- Validate request bodies with Pydantic models from `schemas/`; declare responses with `response_model`.
- Before committing, run `ruff check --fix . && ruff format .` and `pytest` and keep them green.

## Common Commands

```bash
pip install -e ".[dev]"          # install dependencies (including dev extras)
uvicorn <%= pkg %>.main:app --reload --port <%= port %>   # dev server
python -m <%= pkg %>.main        # run module directly
pytest                           # run tests
ruff check .                     # lint
ruff format .                    # format
```
