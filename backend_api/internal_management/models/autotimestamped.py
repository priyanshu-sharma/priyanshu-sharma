from abc import ABC
from datetime import datetime

from pydantic import Field
from pydantic_redis import Model as RedisModel


class AutoTimestamp(RedisModel, ABC):
    """
    An abstract base class for Pydantic-Redis models that automatically manage
    creation and update timestamps.
    """

    install_ts: datetime = Field(default_factory=datetime.now)
    update_ts: datetime = Field(default_factory=datetime.now)

    def pre_save(self):
        """
        Hook that updates the 'update_ts' before saving the model.
        This method will be called automatically by pydantic-redis before saving.
        """
        self.update_ts = datetime.now()

    class Meta:
        abstract = True
