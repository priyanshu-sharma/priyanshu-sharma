from backend_api.internal_management.models.autotimestamped import AutoTimestamp
from backend_api.internal_management.models.usertracking import UserTracking


class Experience(AutoTimestamp, UserTracking):
    title: str
    company: str
    summary: str
    details: str

    class Meta:
        abstract = False
