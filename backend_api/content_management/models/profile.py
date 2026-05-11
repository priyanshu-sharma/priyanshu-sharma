from backend_api.internal_management.models.autotimestamped import AutoTimestamp
from backend_api.internal_management.models.usertracking import UserTracking


class Profile(AutoTimestamp, UserTracking):
    name: str
    role: str
    email: str
    resume_path: str
    availability: str

    class Meta:
        abstract = False
