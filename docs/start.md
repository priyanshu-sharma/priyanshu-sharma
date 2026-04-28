# Project Start Guide

This repository is a FastHTML portfolio site with a small FastAPI API mounted under `/api`.

## What Lives Where

- `app.py` builds the main app and mounts the API sub-app.
- `run.py` is the launcher entrypoint that starts Gunicorn.
- `server_config/` holds server-side configuration:
  - `styles.py` for the global CSS string
  - `gunicorn_conf.py` for Gunicorn settings
  - `health.py` for API routes
- `pages/` contains the page route handlers for the UI.
- `components/` contains reusable UI components.
- `content.py` contains site copy, metadata, and structured content.
- `resume/` contains the resume assets.

## Startup

Preferred local startup:

```bash
uv run python run.py
```

Project shortcut:

```bash
make startapp
```

The server binds to:

- UI: `http://127.0.0.1:4000/`
- API: `http://127.0.0.1:4000/api`

## Runtime

The app runs through:

- Gunicorn
- `uvicorn.workers.UvicornWorker`

## API

The API is mounted under `/api`.

Current route:

- `GET /api/health`

Response:

```json
{ "status": "ok" }
```

## UI Routes

The portfolio UI is registered in `pages/` and served from the root app.

Main routes:

- `/`
- `/projects`
- `/experience`
- `/contact`
- `/blog`
- `/social`
- `/resume`

## Development Commands

Format:

```bash
make format
```

Lint:

```bash
make lint
```

Fix lint issues:

```bash
make fix
```

Run pre-commit:

```bash
make precommit
```

Install pre-commit hooks:

```bash
make precommit-install
```