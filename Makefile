.PHONY: startapp format lint fix precommit precommit-install clean

startapp:
	uv run python run.py

format:
	uv run black .
	uv run ruff format .

lint:
	uv run ruff check .

fix:
	uv run ruff check . --fix
	uv run black .

precommit:
	uv run pre-commit run --all-files

precommit-install:
	uv run pre-commit install

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .ruff_cache
