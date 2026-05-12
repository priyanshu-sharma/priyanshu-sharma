from abc import ABC

from pydantic import Field
from pydantic_redis import Model as RedisModel


class UserTracking(RedisModel, ABC):
    """
    An abstract base class that tracks user creation and updates.
    """

    created_by: str = Field(default="system")
    updated_by: str = Field(default="system")

    class Meta:
        abstract = True
