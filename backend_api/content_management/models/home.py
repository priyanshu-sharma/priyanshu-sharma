from backend_api.internal_management.models.autotimestamped import AutoTimestamp
from backend_api.internal_management.models.usertracking import UserTracking
from typing import List


class Home(AutoTimestamp, UserTracking):
    title: str
    subtitle: str
    badges: List[str]
    philosophy: str
    learning: str
    setup: str

    class Meta:
        abstract = False
