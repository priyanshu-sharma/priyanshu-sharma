import pytest
from backend_api.server_config.env_settings import settings
from databases.init_redis import store


@pytest.fixture(autouse=True)
def setup_test_redis():
    # Force testing mode
    settings.testing = True
    # Re-initialize the store connection to use the new DB
    store.redis_store.flushdb()
    yield
    store.redis_store.flushdb()
