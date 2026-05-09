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

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
