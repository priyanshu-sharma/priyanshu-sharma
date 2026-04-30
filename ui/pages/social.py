from fasthtml.common import *

from ui.components import page_shell
from content import PROFILE, SOCIAL


def social_page():
    return page_shell(
        f"Social | {PROFILE['name']}",
        "/social",
        Section(
            H2(SOCIAL["title"], cls="title"),
            P(SOCIAL["subtitle"], cls="subtitle muted"),
            cls="section",
        ),
        Section(
            Div(
                *(
                    Article(
                        Div(
                            H3(item["name"], cls="section-label"),
                            P(item["description"], cls="muted"),
                            cls="flex-1",
                        ),
                        A(
                            item["cta"],
                            href=item["href"],
                            cls="btn btn-primary",
                            style="margin-top:1rem; align-self: flex-start;",
                        ),
                        cls="card flex-col",
                    )
                    for item in SOCIAL["links"]
                ),
                cls="grid-2",
            ),
            cls="section",
        ),
    )
