from fasthtml.common import *

from ui_design.components import page_shell
from backend_api.content_management.api import get_experiences, get_profile


def experience_page():
    # Fetch from Redis
    experiences = get_experiences()
    profile_obj = get_profile()

    return page_shell(
        f"Experience | {profile_obj.name}",
        "/experience",
        Section(
            H2("Experience", cls="title"),
            P(
                "Platform engineering, analytics infrastructure, and reliability operations.",
                cls="subtitle muted",
            ),
            cls="section",
        ),
        Section(
            Div(
                *(
                    Article(
                        H3(exp.company),
                        H4(exp.title),
                        P(exp.summary, cls="muted", style="margin:0.5rem 0 0;"),
                        P(exp.details, style="margin:1rem 0 0; font-size:0.9rem;"),
                        cls="card",
                    )
                    for exp in experiences
                ),
                cls="grid-2",
            ),
            cls="section",
        ),
    )
