from fasthtml.common import *


def project_card(tag: str, title: str, desc: str, demo_href: str | None = None):
    actions = []
    if demo_href:
        actions.append(
            A("View Project →", href=demo_href, cls="btn btn-primary", target="_blank")
        )
    return Article(
        Header(
            P(tag, cls="section-label", style="margin-bottom: 0.5rem;"),
            H3(title, style="margin:0; font-size:1.25rem;"),
        ),
        P(desc, cls="muted", style="margin:1rem 0 0; font-size:0.95rem;"),
        Div(*actions, cls="btn-row", style="margin-top:1.5rem;") if actions else None,
        cls="card",
    )


def metric_card(value: str, label: str):
    return Div(
        Strong(value, style="font-size: 1.5rem; letter-spacing: -0.02em;"),
        P(
            label,
            cls="muted",
            style="margin:0.25rem 0 0; font-size:0.875rem; text-transform: uppercase; letter-spacing: 0.05em;",
        ),
        cls="metric",
    )
