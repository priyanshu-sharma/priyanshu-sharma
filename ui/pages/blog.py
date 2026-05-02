from fasthtml.common import *

from ui.components import page_shell, project_card
from content import BLOG, PROFILE


def blog_page():
    return page_shell(
        f"Blog | {PROFILE['name']}",
        "/blog",
        Section(
            H2(BLOG["title"], cls="title"),
            P(BLOG["subtitle"], cls="subtitle muted"),
            cls="section",
        ),
        Section(
            Div(
                *(
                    project_card(
                        post["date"],
                        post["title"],
                        post["summary"],
                        demo_href=post["href"],
                    )
                    for post in BLOG["posts"]
                ),
                cls="grid-2",
            ),
            cls="section",
        ),
    )
