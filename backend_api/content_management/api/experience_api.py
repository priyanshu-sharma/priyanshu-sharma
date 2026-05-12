from typing import Any, List, cast

from backend_api.content_management.models.experience import Experience
from databases.primary.content import experience


def get_experiences() -> List[Experience]:
    try:
        return Experience.select()
    except Exception:
        return [
            Experience(
                **{
                    **cast(dict[str, Any], role),
                    "created_by": "system",
                    "updated_by": "system",
                }
            )
            for role in experience.EXPERIENCE["roles"]
        ]
