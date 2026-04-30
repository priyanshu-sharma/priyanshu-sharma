from fasthtml.common import *

from ui.components import page_shell
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
                        Header(
                            H3(role["title"], style="margin:0; font-size:1.25rem;"),
                        ),
                        P(role["summary"], cls="muted", style="margin:0.5rem 0 0;"),
                        P(role["details"], style="margin:1rem 0 0; font-size:0.9rem;"),
                        cls="card",
                    )
                    for role in EXPERIENCE["roles"]
                ),
                cls="grid-2",
            ),
            cls="section",
        ),
    )
