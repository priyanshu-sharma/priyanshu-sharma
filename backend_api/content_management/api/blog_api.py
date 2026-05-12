from typing import Any, List, cast

from backend_api.content_management.models.blog import Blog
from databases.primary.content import blog


def get_blogs() -> List[Blog]:
    try:
        res = Blog.select()
        return res if res is not None else []
    except Exception:
        return [
            Blog(
                **{
                    **cast(dict[str, Any], post),
                    "created_by": "system",
                    "updated_by": "system",
                }
            )
            for post in blog.BLOG["posts"]
        ]
