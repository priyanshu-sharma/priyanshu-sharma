import json
from pathlib import Path
from pydantic_redis import Store, RedisConfig
from backend_api.server_config.settings import (
    REDIS_HOST,
    REDIS_PORT,
    REDIS_DB,
    REDIS_STORE_NAME,
)
from backend_api.content_management.models.blog import Blog
from backend_api.content_management.models.contact import Contact
from backend_api.content_management.models.experience import Experience
from backend_api.content_management.models.home import Home
from backend_api.content_management.models.profile import Profile
from backend_api.content_management.models.project import Project
from backend_api.content_management.models.site import Site
from backend_api.content_management.models.social import Social

# Initialize Redis Store with RedisConfig
config = RedisConfig(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
store = Store(name=REDIS_STORE_NAME, redis_config=config)


store.register_model(Blog)
store.register_model(Contact)
store.register_model(Experience)
store.register_model(Home)
store.register_model(Profile)
store.register_model(Project)
store.register_model(Site)
store.register_model(Social)


def load_fixtures():
    fixtures_dir = Path("backend_api/fixtures")
    model_map = {
        "blog.json": Blog,
        "contact.json": Contact,
        "experiences.json": Experience,
        "home.json": Home,
        "profile.json": Profile,
        "projects.json": Project,
        "site.json": Site,
        "social.json": Social,
    }

    for filename, model in model_map.items():
        filepath = fixtures_dir / filename
        if filepath.exists():
            with open(filepath, "r") as f:
                data = json.load(f)
                for item in data:
                    model.insert(model(**item))
            print(f"Loaded {filename} into {model.__name__}")
        else:
            print(f"Fixture {filename} not found.")


def clear_redis():
    print("Clearing Redis database...")
    store.redis_store.flushall()
