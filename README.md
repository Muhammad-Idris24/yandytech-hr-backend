# YandyTech HR SaaS Backend

A secure, multi-tenant HR SaaS backend built with FastAPI, PostgreSQL, and Auth0.

## Quick start

```bash
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

## Features in this foundation

- Auth0-compatible auth structure
- tenant-aware authorization helpers
- PostgreSQL connection layer
- health check endpoint
- organization and employee API foundations
- structured logging and configuration support
