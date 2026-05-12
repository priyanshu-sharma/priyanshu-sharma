from backend_api.content_management.models.profile import Profile
from databases.primary.content import profile


def get_profile() -> Profile:
    try:
        data = Profile.select()
        if data:
            return data[0]
        raise Exception("No profile found")
    except Exception:
        return Profile(
            **{**profile.PROFILE, "created_by": "system", "updated_by": "system"}
        )
