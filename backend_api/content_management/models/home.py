from typing import List
from uuid import uuid4

from backend_api.internal_management.models.autotimestamped import AutoTimestamp
from backend_api.internal_management.models.usertracking import UserTracking


class Home(AutoTimestamp, UserTracking):
    _primary_key_field: str = "uuid"
    uuid: str = uuid4().hex
    active: bool = True
    title: str
    subtitle: str
    badges: List[str]
    philosophy: str
    learning: str
    setup: str

    class Meta:
        abstract = False
