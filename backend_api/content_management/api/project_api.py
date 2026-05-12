from typing import Any, List, cast

from backend_api.content_management.models.project import Project
from databases.primary.content import projects


def get_projects() -> List[Project]:
    try:
        return Project.select()
    except Exception:
        return [
            Project(
                **{
                    **cast(dict[str, Any], item),
                    "created_by": "system",
                    "updated_by": "system",
                }
            )
            for item in projects.PROJECTS["items"]
        ]
