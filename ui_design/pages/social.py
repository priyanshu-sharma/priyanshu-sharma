from fasthtml.common import *

from ui_design.components import page_shell
from backend_api.content_management.models.social import Social
from backend_api.content_management.models.profile import Profile


def social_page():
    social_items = Social.select()
    profile_obj = Profile.select()[0]

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
