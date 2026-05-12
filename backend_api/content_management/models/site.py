from uuid import uuid4

from backend_api.internal_management.models.autotimestamped import AutoTimestamp
from backend_api.internal_management.models.usertracking import UserTracking


class Site(AutoTimestamp, UserTracking):
    _primary_key_field: str = "uuid"
    uuid: str = uuid4().hex
    active: bool = True
    name: str
    title: str
    description: str
    author: str
    keywords: str
    url: str
    api_title: str
    api_description: str
    api_version: str

    class Meta:
        abstract = False
