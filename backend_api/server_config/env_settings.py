from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

# Determine the project root directory
# env_settings.py is at backend_api/server_config/env_settings.py
# So, project root is 2 levels up from this file's location.
ENV_SETTINGS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = ENV_SETTINGS_DIR.parent.parent


class Settings(BaseSettings):
    debug: bool = False
    secret_key: str = "django-insecure-default"
    project_root: Path = PROJECT_ROOT
    testing: bool = False

    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0
    redis_store_name: str = "portfolio_store"

    def __init__(self, **values):
        super().__init__(**values)
        if self.testing:
            self.redis_db = 1  # Use DB 1 for testing

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
