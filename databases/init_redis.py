import json
from pathlib import Path
from pydantic_redis import Store, RedisConfig
from backend_api.server_config.settings import (
    REDIS_HOST,
    REDIS_PORT,
    REDIS_DB,
    REDIS_STORE_NAME,
)

# Import models
from backend_api.content_management.models.blog import Blog
from backend_api.content_management.models.contact import Contact
from backend_api.content_management.models.experience import Experience
from backend_api.content_management.models.home import Home
from backend_api.content_management.models.profile import Profile
from backend_api.content_management.models.project import Project
from backend_api.content_management.models.site import Site
from backend_api.content_management.models.social import Social

# Configuration
config = RedisConfig(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
store = Store(name=REDIS_STORE_NAME, redis_config=config)

MODELS = [Blog, Contact, Experience, Home, Profile, Project, Site, Social]


def verify_redis():
    try:
        store.redis_store.ping()
        print("Successfully connected to Redis.")
    except Exception as e:
        print(f"Failed to connect to Redis: {e}")
        raise


# Register all models
for model in MODELS:
    store.register_model(model)


def load_fixtures():
    verify_redis()
    fixtures_dir = Path("databases/primary/fixtures")

    # Mapping filename pattern to Model
    fixture_map = {
        "blog.json": Blog,
        "contact.json": Contact,
        "experiences.json": Experience,
        "home.json": Home,
        "profile.json": Profile,
        "projects.json": Project,
        "site.json": Site,
        "social.json": Social,
    }

    for filename, model in fixture_map.items():
        filepath = fixtures_dir / filename
        if filepath.exists():
            with open(filepath, "r") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    data = [data]

                for item in data:
                    # Simply inserting; pydantic-redis seems to handle some key logic internally
                    # but our select() attempt failed.
                    try:
                        model.insert(model(**item))
                    except Exception:
                        pass  # Silently ignore insertion errors for existing keys
            print(f"Processed {filename}")
        else:
            print(f"Fixture {filename} not found.")


def clear_redis():
    print("Clearing Redis database...")
    store.redis_store.flushall()
