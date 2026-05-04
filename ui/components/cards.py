from fasthtml.common import *


def project_card(tag: str, title: str, desc: str, demo_href: str | None = None):
    actions = []
    if demo_href:
        actions.append(
            A("View Project →", href=demo_href, cls="btn btn-primary", target="_blank")
        )
    return Article(
        H3(tag),
        H4(title),
        P(desc),
        Div(*actions, cls="btn-row") if actions else None,
        cls="card",
    )
