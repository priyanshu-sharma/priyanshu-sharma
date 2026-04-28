from fasthtml.common import *

from content import PROFILE

from .navigation import NAV_ITEMS


def page_shell(title: str, active_path: str, *content):
    nav_links = []
    for href, label in NAV_ITEMS:
        cls = "btn btn-primary" if href == active_path else "btn"
        nav_links.append(A(label, href=href, cls=cls))

    return (
        Title(title),
        Div(
            Header(
                Div(
                    Div(cls="avatar"),
                    Div(
                        P(
                            PROFILE["role"],
                            cls="muted",
                            style="margin:0;font-size:0.85rem;",
                        ),
                        H1(PROFILE["name"], cls="h1"),
                    ),
                    cls="profile",
                ),
                Div(*nav_links, cls="nav"),
                cls="header",
            ),
            *content,
            Footer(
                P(PROFILE["availability"], cls="muted", style="margin:0;"),
                Div(
                    A("Email", href=f"mailto:{PROFILE['email']}", cls="btn"),
                    A("Resume", href=PROFILE["resume_path"], cls="btn"),
                    cls="btn-row",
                ),
                cls="footer",
            ),
            cls="container",
        ),
    )
