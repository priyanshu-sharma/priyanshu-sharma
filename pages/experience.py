from fasthtml.common import *

from components import page_shell
from content import EXPERIENCE, PROFILE


def experience_page():
    return page_shell(
        f"Experience | {PROFILE['name']}",
        "/experience",
        Section(
            H2(EXPERIENCE["title"], cls="title"),
            P(EXPERIENCE["subtitle"], cls="subtitle muted"),
            cls="section",
        ),
        Section(
            Div(
                *(
                    Article(
                        H3(role["title"], cls="section-label"),
                        P(role["summary"], cls="muted"),
                        P(role["details"], style="margin-top:0.6rem;"),
                        cls="card",
                    )
                    for role in EXPERIENCE["roles"]
                ),
                cls="grid-2",
            ),
            cls="section",
        ),
    )
