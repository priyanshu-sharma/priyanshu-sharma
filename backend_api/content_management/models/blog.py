from backend_api.internal_management.models.autotimestamped import AutoTimestamp
from backend_api.internal_management.models.usertracking import UserTracking


class Blog(AutoTimestamp, UserTracking):
    date: str
    title: str
    summary: str
    href: str

    class Meta:
        abstract = False
