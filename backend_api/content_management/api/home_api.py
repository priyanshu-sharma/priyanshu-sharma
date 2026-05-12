from backend_api.content_management.models.home import Home
from databases.primary.content import home


def get_home() -> Home:
    try:
        return Home.select()[0]
    except Exception:
        return Home(**{**home.HOME, "created_by": "system", "updated_by": "system"})
