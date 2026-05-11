from backend_api.internal_management.models.autotimestamped import AutoTimestamp
from backend_api.internal_management.models.usertracking import UserTracking


class Project(AutoTimestamp, UserTracking):
    """
    Model representing a project item.
    """

    tag: str
    title: str
    desc: str
    demo_href: str

    class Meta:
        abstract = False
