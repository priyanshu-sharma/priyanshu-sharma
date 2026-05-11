from fasthtml.common import *

from ui_design.components import page_shell
from backend_api.content_management.api import get_social, get_profile


def social_page():
    social_items = get_social()
    profile_obj = get_profile()

    return page_shell(
        f"Social | {profile_obj.name}",
        "/social",
        Section(
            H2("Social", cls="title"),
            P("Connect with me across various platforms.", cls="subtitle muted"),
            cls="section",
        ),
        Section(
            Div(
                *(
                    Article(
                        H3("Social Platform"),
                        H4(item.name),
                        P(item.description, cls="muted"),
                        A(
                            item.cta,
                            href=item.href,
                            cls="btn btn-primary",
                            style="margin-top:1rem; align-self: flex-start;",
                        ),
                        cls="card",
                    )
                    for item in social_items
                ),
                cls="grid-2",
            ),
            cls="section",
        ),
    )
