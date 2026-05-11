from uuid import uuid4
from backend_api.internal_management.models.autotimestamped import AutoTimestamp
from backend_api.internal_management.models.usertracking import UserTracking


class Project(AutoTimestamp, UserTracking):
    _primary_key_field: str = "uuid"
    uuid: str = uuid4().hex
    active: bool = True
    tag: str
    title: str
    desc: str
    demo_href: str

    class Meta:
        abstract = False
