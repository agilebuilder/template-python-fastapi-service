# <%= projectName %>

<% var pkg = packageDir.charAt(0) === '<' ? snakeCase(projectName) : packageDir -%>
<%= description %>

An async API service built on FastAPI + SQLAlchemy 2.x (asyncio) + Pydantic v2, with a src layout and dependency/packaging management via pyproject.toml (hatchling).

## Tech Stack

- Python <%= pythonVersion %>
- FastAPI (web framework) + Uvicorn (ASGI server)
- SQLAlchemy 2.x async ORM (SQLite + aiosqlite by default; switchable to other databases)
- Pydantic v2 + pydantic-settings (data validation and configuration)
- pytest + pytest-asyncio + httpx AsyncClient (async testing)
- Ruff (lint and formatting)

## Project Structure

```
├── src/<%= pkg %>/          # Python package
│   ├── main.py             # App entry: create_app() factory, uvicorn startup
│   ├── api/                # Routing layer
│   │   ├── router.py       # Router aggregation
│   │   └── routes/         # health / items example routes
│   ├── core/               # Settings (pydantic-settings)
│   ├── db/                 # Async engine and session management
│   ├── models/             # SQLAlchemy ORM models
│   ├── schemas/            # Pydantic request/response models
│   └── services/           # Business logic layer
├── tests/                  # pytest + httpx AsyncClient example tests
├── pyproject.toml          # Project metadata, dependencies, pytest/ruff config
└── .env.example            # Environment variable example
```

## Create a Project from This Template

```bash
ag create --git-url <repo-url> --target <directory>
```

### Template Variables

| Variable | Description | Default |
| --- | --- | --- |
| projectName | Project name (distribution name) | demo-api |
| packageDir | Python package directory name | Derived from projectName in snake_case |
| description | Project description | A FastAPI service |
| author | Author | (empty) |
| port | Server port | 8000 |
| pythonVersion | Python version (3.11 / 3.12) | 3.12 |

## Quick Start

```bash
# Create a virtual environment and install dependencies (including dev extras)
python -m venv .venv
source .venv/Scripts/activate    # Windows Git Bash; use source .venv/bin/activate on macOS/Linux
pip install -e ".[dev]"

# Prepare environment variables (optional; all have defaults)
cp .env.example .env

# Start the dev server (creates tables automatically; default port <%= port %>)
uvicorn <%= pkg %>.main:app --reload --port <%= port %>
```

Once running:

- Health check: http://localhost:<%= port %>/health
- Interactive docs: http://localhost:<%= port %>/docs

You can also run the module directly:

```bash
python -m <%= pkg %>.main
```

## Common Commands

```bash
# Run tests
pytest

# Lint check / auto-fix
ruff check .
ruff check --fix .

# Format
ruff format .
```

## Configuration

Configuration lives in `src/<%= pkg %>/core/config.py` and can be overridden via environment variables or a `.env` file:

| Variable | Description | Default |
| --- | --- | --- |
| APP_NAME | Application name | <%= projectName %> |
| DEBUG | Debug mode | false |
| DATABASE_URL | Database connection URL | sqlite+aiosqlite:///./app.db |
| PORT | Server port | <%= port %> |

## License

MIT
