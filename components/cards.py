from fasthtml.common import *


def project_card(tag: str, title: str, desc: str, demo_href: str | None = None):
    actions = []
    if demo_href:
        actions.append(
            A("View Demo", href=demo_href, cls="btn btn-primary", target="_blank")
        )
    return Article(
        P(tag, cls="muted", style="margin:0 0 0.3rem;font-size:0.75rem;"),
        P(title, style="margin:0 0 0.4rem;font-size:0.95rem;font-weight:600;"),
        P(desc, cls="muted", style="margin:0;font-size:0.9rem;"),
        Div(*actions, cls="btn-row", style="margin-top:1rem;") if actions else None,
        cls="card",
    )


def metric_card(value: str, label: str):
    return Div(
        Strong(value),
        P(label, cls="muted", style="margin:0.2rem 0 0;font-size:0.78rem;"),
        cls="metric",
    )
