from fasthtml.common import *

from components import page_shell, project_card
from content import PROFILE, PROJECTS


def projects_page():
    return page_shell(
        f"Projects | {PROFILE['name']}",
        "/projects",
        Section(
            H2(PROJECTS["title"], cls="title"),
            P(PROJECTS["subtitle"], cls="subtitle muted"),
            cls="section",
        ),
        Section(
            Div(
                *(
                    project_card(
                        item["tag"], item["title"], item["desc"], item.get("demo_href")
                    )
                    for item in PROJECTS["items"]
                ),
                cls="grid-2",
            ),
            cls="section",
        ),
    )
