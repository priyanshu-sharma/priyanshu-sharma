from fasthtml.common import H2, H3, H4, A, Article, Div, P, Section

from backend_api.content_management.api import get_profile, get_social
from ui_design.components import page_shell


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
