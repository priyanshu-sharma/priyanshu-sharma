import os

from backend_api.server_config.settings import DATABASES


def test_database_configuration():
    # Verify the database is using PostgreSQL (or expected engine)
    db_engine = DATABASES["default"].get("ENGINE", "")
    assert "postgresql" in db_engine or "sqlite" in db_engine

    # Check if DATABASE_URL is set in the environment
    assert "DATABASE_URL" in os.environ
    print(f"Database engine detected: {db_engine}")
