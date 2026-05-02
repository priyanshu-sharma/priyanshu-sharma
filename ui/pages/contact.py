from fasthtml.common import *

from ui.components import page_shell
from content import CONTACT, PROFILE


def contact_page():
    return page_shell(
        f"Contact | {PROFILE['name']}",
        "/contact",
        Section(
            H2(CONTACT["title"], cls="title"),
            P(
                "Let's connect for opportunities, consulting, or technical discussions.",
                cls="subtitle muted",
            ),
            cls="section",
        ),
        Section(
            Div(
                Div(
                    H3("Phone"),
                    Div(
                        P(
                            "+1 (555) 012-3456",
                            cls="muted",
                            style="margin-bottom: 1.8rem;",
                        ),
                        Button(
                            "Copy",
                            cls="btn btn-primary",
                            onclick="copyToClipboard('+1 (555) 012-3456', this)",
                        ),
                        style="display:flex; flex-direction:column; align-items:start;",
                    ),
                    cls="card",
                ),
                Div(
                    H3("Personal Email"),
                    Div(
                        P(
                            "priyanshu.personal@example.com",
                            cls="muted",
                            style="margin-bottom: 1.8rem;",
                        ),
                        Button(
                            "Copy",
                            cls="btn btn-primary",
                            onclick="copyToClipboard('priyanshu.personal@example.com', this)",
                        ),
                        style="display:flex; flex-direction:column; align-items:start;",
                    ),
                    cls="card",
                ),
                Div(
                    H3("Location"),
                    P("New York City, NY", cls="muted"),
                    cls="card",
                ),
                style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;",
            ),
            cls="section",
        ),
    )
