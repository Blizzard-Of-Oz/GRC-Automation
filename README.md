# GRC Automation Platform (Initial Scaffold)

Backend foundation for an on-prem continuous compliance automation platform integrated with Eramba.

## Tech Stack
- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy 2.x
- Alembic
- Docker Compose

## Repository Structure

```text
.
├── app/
│   ├── api/              # HTTP endpoints
│   ├── connectors/       # External tool connector abstractions (placeholders)
│   ├── core/             # Configuration and shared internals
│   ├── database/         # Engine, sessions, SQLAlchemy base
│   ├── domain/           # Domain language and entities (placeholder)
│   ├── eramba_sync/      # Sync workflows to Eramba (placeholder)
│   ├── jobs/             # Background job stubs (placeholder)
│   ├── normalization/    # Evidence normalization package (placeholder)
│   └── rules/            # Compliance rules engine package (placeholder)
├── alembic/              # Database migration environment
├── docs/                 # Project docs
├── tests/                # Test suite
├── PRODUCT_SCOPE.md      # Product vision, MVP, and non-goals
├── docker-compose.yml    # Local dev stack (api + postgres)
└── .env.example          # Environment variables template
```

## Quick Start

1. Copy environment template:
   ```bash
   cp .env.example .env
   ```

2. Build and run services:
   ```bash
   docker compose up --build
   ```

3. Verify healthcheck:
   ```bash
   curl http://localhost:8000/api/v1/health
   ```

Expected response:
```json
{"status":"ok","service":"grc-automation-platform"}
```

## Local (without Docker)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
cp .env.example .env
uvicorn app.main:app --reload
```

## Alembic Usage

Create a migration:
```bash
alembic revision --autogenerate -m "init"
```

Apply migrations:
```bash
alembic upgrade head
```

## Current Scope Status
- ✅ Backend scaffold and modular package boundaries.
- ✅ Environment-based settings.
- ✅ Docker Compose with API + PostgreSQL.
- ✅ Health endpoint and smoke test.
- ✅ Alembic foundation.
- ⏳ Connectors, normalization flows, rule engine, and Eramba sync are placeholders for incremental implementation.
