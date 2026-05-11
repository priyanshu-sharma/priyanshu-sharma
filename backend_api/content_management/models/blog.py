from uuid import uuid4
from backend_api.internal_management.models.autotimestamped import AutoTimestamp
from backend_api.internal_management.models.usertracking import UserTracking


class Blog(AutoTimestamp, UserTracking):
    _primary_key_field: str = "uuid"
    uuid: str = uuid4().hex
    active: bool = True
    date: str
    title: str
    summary: str
    href: str

    class Meta:
        abstract = False
