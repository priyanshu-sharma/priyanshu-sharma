from fasthtml.common import *
from content import PROFILE

NAV_ITEMS = [
    ("/", "Home"),
    ("/projects", "Projects"),
    ("/experience", "Experience"),
    ("/blog", "Blog"),
    ("/social", "Social"),
    ("/contact", "Contact"),
]


def project_card(tag: str, title: str, desc: str):
    return Article(
        P(tag, cls="muted", style="margin:0 0 0.3rem;font-size:0.75rem;"),
        P(title, style="margin:0 0 0.4rem;font-size:0.95rem;font-weight:600;"),
        P(desc, cls="muted", style="margin:0;font-size:0.9rem;"),
        cls="card",
    )


def metric_card(value: str, label: str):
    return Div(
        Strong(value),
        P(label, cls="muted", style="margin:0.2rem 0 0;font-size:0.78rem;"),
        cls="metric",
    )


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
                        P(PROFILE["role"], cls="muted", style="margin:0;font-size:0.85rem;"),
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
