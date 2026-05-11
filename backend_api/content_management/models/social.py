from backend_api.internal_management.models.autotimestamped import AutoTimestamp
from backend_api.internal_management.models.usertracking import UserTracking


class Social(AutoTimestamp, UserTracking):
    name: str
    description: str
    href: str
    cta: str

    class Meta:
        abstract = False
