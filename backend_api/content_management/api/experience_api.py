from typing import Any, List, cast

from backend_api.content_management.models.experience import Experience
from databases.primary.content import experience


def get_experiences() -> List[Experience]:
    try:
        res = Experience.select()
        return res if res is not None else []
    except Exception:
        return [
            Experience(
                **{
                    **cast(dict[str, Any], exp),
                    "created_by": "system",
                    "updated_by": "system",
                }
            )
            for exp in experience.EXPERIENCE["roles"]
        ]
