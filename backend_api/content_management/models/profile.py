from uuid import uuid4

from pydantic import EmailStr

from backend_api.internal_management.models.autotimestamped import AutoTimestamp
from backend_api.internal_management.models.usertracking import UserTracking


class Profile(AutoTimestamp, UserTracking):
    _primary_key_field: str = "uuid"
    uuid: str = uuid4().hex
    active: bool = True
    name: str
    role: str
    email: EmailStr
    resume_path: str
    availability: str

    class Meta:
        abstract = False
