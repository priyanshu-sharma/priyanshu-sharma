from fasthtml.common import *

from ui_design.components import page_shell, project_card
from backend_api.content_management.models.project import Project
from backend_api.content_management.models.profile import Profile


def projects_page():
    # Fetch from Redis
    items = Project.select()
    profile_obj = Profile.select()[0]

    # Static fallback titles if needed
    title = "Projects"
    subtitle = "Real-world data engineering and platform reliability projects."

    # Map the ORM objects
    data_items = [
        {"tag": p.tag, "title": p.title, "desc": p.desc, "demo_href": p.demo_href}
        for p in items
    ]

    first = data_items[0]
    second = data_items[1]
    third = data_items[2]
    fourth = data_items[3]
    fifth = data_items[4]
    sixth = data_items[5]
    rest = data_items[6:]
    return page_shell(
        f"Projects | {profile_obj.name}",
        "/projects",
        Section(
            H2(title, cls="title"),
            P(subtitle, cls="subtitle muted"),
            cls="section",
        ),
        Section(
            # Project 1 (70/30)
            Div(
                Div(
                    H3(first["tag"], style="margin: 0;"),
                    H4(
                        first["title"], style="font-size: 1.7rem; margin: 0 0 0.5rem 0;"
                    ),
                    P(first["desc"], style="font-size: 1.1rem; margin: 0;"),
                    cls="bento-card",
                    style="flex: 7; gap: 0.25rem;",
                ),
                Div(
                    A(
                        "View Project →",
                        href=first["demo_href"],
                        cls="btn btn-primary",
                        style="padding: 1rem 1.5rem;",
                    ),
                    cls="bento-card",
                    style="flex: 3; justify-content: center; align-items: center;",
                ),
                style="display: flex; gap: 1.5rem; margin-bottom: 1.5rem;",
            ),
            # Project 2 (30/70)
            Div(
                Div(
                    A(
                        "View Project →",
                        href=second["demo_href"],
                        cls="btn btn-primary",
                        style="padding: 1rem 1.5rem;",
                    ),
                    cls="bento-card",
                    style="flex: 3; justify-content: center; align-items: center;",
                ),
                Div(
                    H3(second["tag"], style="margin: 0;"),
                    H4(
                        second["title"],
                        style="font-size: 1.7rem; margin: 0 0 0.5rem 0;",
                    ),
                    P(second["desc"], style="font-size: 1.1rem; margin: 0;"),
                    cls="bento-card",
                    style="flex: 7; gap: 0.25rem;",
                ),
                style="display: flex; gap: 1.5rem; margin-bottom: 1.5rem;",
            ),
            # Project 3 (70/30)
            Div(
                Div(
                    H3(third["tag"], style="margin: 0;"),
                    H4(
                        third["title"], style="font-size: 1.7rem; margin: 0 0 0.5rem 0;"
                    ),
                    P(third["desc"], style="font-size: 1.1rem; margin: 0;"),
                    cls="bento-card",
                    style="flex: 7; gap: 0.25rem;",
                ),
                Div(
                    A(
                        "View Project →",
                        href=third["demo_href"],
                        cls="btn btn-primary",
                        style="padding: 1rem 1.5rem;",
                    ),
                    cls="bento-card",
                    style="flex: 3; justify-content: center; align-items: center;",
                ),
                style="display: flex; gap: 1.5rem; margin-bottom: 1.5rem;",
            ),
            # Project 4 (30/70)
            Div(
                Div(
                    A(
                        "View Project →",
                        href=fourth["demo_href"],
                        cls="btn btn-primary",
                        style="padding: 1rem 1.5rem;",
                    ),
                    cls="bento-card",
                    style="flex: 3; justify-content: center; align-items: center;",
                ),
                Div(
                    H3(fourth["tag"], style="margin: 0;"),
                    H4(
                        fourth["title"],
                        style="font-size: 1.7rem; margin: 0 0 0.5rem 0;",
                    ),
                    P(fourth["desc"], style="font-size: 1.1rem; margin: 0;"),
                    cls="bento-card",
                    style="flex: 7; gap: 0.25rem;",
                ),
                style="display: flex; gap: 1.5rem; margin-bottom: 1.5rem;",
            ),
            # Project 5 (70/30)
            Div(
                Div(
                    H3(fifth["tag"], style="margin: 0;"),
                    H4(
                        fifth["title"], style="font-size: 1.7rem; margin: 0 0 0.5rem 0;"
                    ),
                    P(fifth["desc"], style="font-size: 1.1rem; margin: 0;"),
                    cls="bento-card",
                    style="flex: 7; gap: 0.25rem;",
                ),
                Div(
                    A(
                        "View Project →",
                        href=fifth["demo_href"],
                        cls="btn btn-primary",
                        style="padding: 1rem 1.5rem;",
                    ),
                    cls="bento-card",
                    style="flex: 3; justify-content: center; align-items: center;",
                ),
                style="display: flex; gap: 1.5rem; margin-bottom: 1.5rem;",
            ),
            # Project 6 (30/70)
            Div(
                Div(
                    A(
                        "View Project →",
                        href=sixth["demo_href"],
                        cls="btn btn-primary",
                        style="padding: 1rem 1.5rem;",
                    ),
                    cls="bento-card",
                    style="flex: 3; justify-content: center; align-items: center;",
                ),
                Div(
                    H3(sixth["tag"], style="margin: 0;"),
                    H4(
                        sixth["title"], style="font-size: 1.7rem; margin: 0 0 0.5rem 0;"
                    ),
                    P(sixth["desc"], style="font-size: 1.1rem; margin: 0;"),
                    cls="bento-card",
                    style="flex: 7; gap: 0.25rem;",
                ),
                style="display: flex; gap: 1.5rem; margin-bottom: 1.5rem;",
            ),
            # Remaining Projects
            Div(
                *(
                    project_card(
                        item["tag"], item["title"], item["desc"], item.get("demo_href")
                    )
                    for item in rest
                ),
                cls="bento-grid",
            ),
            cls="section",
        ),
    )
