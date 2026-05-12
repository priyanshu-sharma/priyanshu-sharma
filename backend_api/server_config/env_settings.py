from pathlib import Path
from typing import Literal, Optional

from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_SETTINGS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = ENV_SETTINGS_DIR.parent.parent


class Settings(BaseSettings):
    name: Literal["DEV", "TESTING", "PRE_PROD", "PROD"] = "DEV"
    debug: bool = False
    secret_key: str = "ac7346a0-9b1b-41a0-b607-811e616064e8"
    project_root: Path = PROJECT_ROOT
    redis_user: Optional[str] = None
    redis_password: Optional[str] = None
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0
    redis_store_name: str = "portfolio_store"
    model_config = SettingsConfigDict(env_file=".env", env_prefix="APP_")

    def __init__(self, **values):
        super().__init__(**values)
        print("-------------{}--------------".format(self.name))
        if self.name == "PROD":
            self.debug = False
            self.redis_db = 0
        elif self.name == "PRE_PROD":
            self.debug = True
            self.redis_db = 2
        elif self.name == "TESTING":
            self.debug = True
            self.redis_db = 1
        else:
            self.debug = True
            self.redis_db = 0


settings = Settings()
