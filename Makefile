.PHONY: startapp format lint fix precommit precommit-install clean test migrate makemigrations_content_management

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
	rm -rf .ruff_cache .pytest_cache

test:
	uv run pytest tests/

migrate:
	uv run python manage.py migrate

show-migrations:
	uv run python manage.py showmigrations

migrate:
	uv run python manage.py showmigrations
	uv run python manage.py migrate

make-migrations:
	uv run python manage.py showmigrations
	uv run python manage.py makemigrations
	uv run python manage.py migrate
	uv run python manage.py showmigrations
