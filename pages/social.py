from fasthtml.common import *

from components import page_shell
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
                        H3(item["name"], cls="section-label"),
                        P(item["description"], cls="muted"),
                        A(
                            item["cta"],
                            href=item["href"],
                            cls="btn",
                            style="margin-top:0.8rem;",
                        ),
                        cls="card",
                    )
                    for item in SOCIAL["links"]
                ),
                cls="grid-2",
            ),
            cls="section",
        ),
    )
