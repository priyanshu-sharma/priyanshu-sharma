from typing import Any, List, cast

from backend_api.content_management.models.project import Project
from databases.primary.content import projects


def get_projects() -> List[Project]:
    try:
        res = Project.select()
        return res if res is not None else []
    except Exception:
        return [
            Project(
                **{
                    **cast(dict[str, Any], proj),
                    "created_by": "system",
                    "updated_by": "system",
                }
            )
            for proj in projects.PROJECTS["items"]
        ]
