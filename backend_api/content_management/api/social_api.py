from typing import Any, List, cast

from backend_api.content_management.models.social import Social
from databases.primary.content import social


def get_social() -> List[Social]:
    try:
        res = Social.select()
        return res if res is not None else []
    except Exception:
        return [
            Social(
                **{
                    **cast(dict[str, Any], link),
                    "created_by": "system",
                    "updated_by": "system",
                }
            )
            for link in social.SOCIAL["links"]
        ]
