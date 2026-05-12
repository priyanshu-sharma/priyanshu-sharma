from backend_api.content_management.models.profile import Profile
from databases.primary.content import profile


def get_profile() -> Profile:
    try:
        return Profile.select()[0]
    except Exception:
        return Profile(
            **{**profile.PROFILE, "created_by": "system", "updated_by": "system"}
        )
