from fasthtml.common import H2, H3, H4, A, Div, P, Section

from backend_api.content_management.api import get_profile, get_projects
from ui_design.components import page_shell, project_card


def projects_page():
    # Fetch from Redis
    items = get_projects() or []
    profile_obj = get_profile()

    # Static fallback titles if needed
    title = "Projects"
    subtitle = "Real-world data engineering and platform reliability projects."

    # Pad items to at least 6 for the grid layout
    while len(items) < 6:
        items.append(None)

    # Use objects directly
    first, second, third, fourth, fifth, sixth = items[:6]
    rest = items[6:]

    def project_div(item, reverse=False):
        if not item:
            return Div()
        card = Div(
            Div(
                H3(item.tag, style="margin: 0;"),
                H4(item.title, style="font-size: 1.7rem; margin: 0 0 0.5rem 0;"),
                P(item.desc, style="font-size: 1.1rem; margin: 0;"),
                cls="bento-card",
                style="flex: 7; gap: 0.25rem;",
            ),
            Div(
                A(
                    "View Project →",
                    href=item.demo_href,
                    cls="btn btn-primary",
                    style="padding: 1rem 1.5rem;",
                ),
                cls="bento-card",
                style="flex: 3; justify-content: center; align-items: center;",
            ),
            style="display: flex; gap: 1.5rem; margin-bottom: 1.5rem; flex-direction: "
            + ("row-reverse" if reverse else "row"),
        )
        return card

    return page_shell(
        f"Projects | {profile_obj.name}",
        "/projects",
        Section(
            H2(title, cls="title"),
            P(subtitle, cls="subtitle muted"),
            cls="section",
        ),
        Section(
            project_div(first),
            project_div(second, reverse=True),
            project_div(third),
            project_div(fourth, reverse=True),
            project_div(fifth),
            project_div(sixth, reverse=True),
            Div(
                *(project_card(item) for item in rest if item),
                cls="bento-grid",
            ),
            cls="section",
        ),
    )
