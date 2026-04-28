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
	rm -rf __pycache__ components/__pycache__ pages/__pycache__ server_config/__pycache__ .ruff_cache
