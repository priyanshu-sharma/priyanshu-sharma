from backend_api.content_management.models.home import Home
from databases.primary.content import home


def get_home() -> Home:
    try:
        data = Home.select()
        if data:
            return data[0]
        raise Exception("No home data found")
    except Exception:
        return Home(**{**home.HOME, "created_by": "system", "updated_by": "system"})
