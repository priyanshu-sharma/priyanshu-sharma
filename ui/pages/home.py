from fasthtml.common import *

from ui.components import metric_card, page_shell
from content import HOME, PROFILE


def home_page():
    return page_shell(
        f"{PROFILE['name']} | {PROFILE['role']}",
        "/",
        Section(
            H2(HOME["title"], cls="title"),
            P(HOME["subtitle"], cls="subtitle muted", style="margin-bottom: 1.5rem;"),
            Div(*(Span(item, cls="badge") for item in HOME["badges"]), cls="badge-row"),
            cls="section",
        ),
        Section(
            H3(HOME["snapshot_title"], cls="section-label"),
            Div(
                *(
                    metric_card(metric["value"], metric["label"])
                    for metric in HOME["metrics"]
                ),
                cls="metric-grid",
            ),
            cls="section",
        ),
    )
