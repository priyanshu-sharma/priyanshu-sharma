from uuid import uuid4
from backend_api.internal_management.models.autotimestamped import AutoTimestamp
from backend_api.internal_management.models.usertracking import UserTracking


class Social(AutoTimestamp, UserTracking):
    _primary_key_field: str = "uuid"
    uuid: str = uuid4().hex
    active: bool = True
    name: str
    description: str
    href: str
    cta: str

    class Meta:
        abstract = False
