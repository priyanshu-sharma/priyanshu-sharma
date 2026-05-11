from backend_api.internal_management.models.autotimestamped import AutoTimestamp
from backend_api.internal_management.models.usertracking import UserTracking


class Contact(AutoTimestamp, UserTracking):
    title: str
    subtitle: str

    class Meta:
        abstract = False
