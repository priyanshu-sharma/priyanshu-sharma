from fasthtml.common import H2, H3, A, Button, Div, P, Section, Span

from backend_api.content_management.api import get_home, get_profile
from ui_design.components import page_shell


def home_page():
    # Fetch from Redis
    home_obj = get_home()
    profile_obj = get_profile()

    return page_shell(
        f"{profile_obj.name} | {profile_obj.role}",
        "/",
        Section(
            H2(home_obj.title, cls="title"),
            P(home_obj.subtitle, cls="subtitle muted", style="margin-bottom: 1.5rem;"),
            Div(
                *(Span(item, cls="badge") for item in home_obj.badges), cls="badge-row"
            ),
            cls="section",
        ),
        Section(
            Div(
                # Top Row: Me, Experience, Resume
                Div(
                    Div(H3("Me"), P(f"{profile_obj.name} 👋"), cls="bento-card"),
                    Div(H3("Experience"), P("7+ Years"), cls="bento-card"),
                    Div(
                        H3("Resume"),
                        A(
                            "View PDF",
                            href=profile_obj.resume_path,
                            cls="btn btn-primary",
                        ),
                        cls="bento-card",
                    ),
                    cls="top-row",
                ),
                # Philosophy (Full Width)
                Div(
                    H3("Philosophy"),
                    P(home_obj.philosophy),
                    cls="bento-card",
                    style="margin-bottom: 1.5rem;",
                ),
                # Toolkit & Workspace (Shared Width)
                Div(
                    Div(
                        H3("Toolkit"),
                        P(", ".join(home_obj.badges)),
                        cls="bento-card",
                        style="flex: 1;",
                    ),
                    Div(
                        H3("Workspace"),
                        P(home_obj.setup),
                        cls="bento-card",
                        style="flex: 1;",
                    ),
                    style="display: flex; gap: 1.5rem; margin-bottom: 1.5rem;",
                ),
                # Location & Learning (30/70 split)
                Div(
                    Div(
                        H3("Location"),
                        P("New York City, NY"),
                        A(
                            "View Map",
                            href="https://www.google.com/maps/place/New+York,+NY",
                            cls="btn btn-primary",
                            style="margin-top: 0.5rem;",
                        ),
                        cls="bento-card",
                        style="flex: 3;",
                    ),
                    Div(
                        H3("Learning"),
                        P(home_obj.learning),
                        cls="bento-card",
                        style="flex: 7;",
                    ),
                    style="display: flex; gap: 1.5rem; margin-bottom: 1.5rem;",
                ),
                # Bento Grid (Remaining Items: Status, Projects, Connect)
                Div(
                    Div(H3("Status"), P("Open for consulting"), cls="bento-card"),
                    Div(H3("Projects"), P("6+ Production pipelines"), cls="bento-card"),
                    Div(
                        H3("Connect"),
                        Button(
                            "Copy Email",
                            cls="btn btn-primary",
                            onclick=f"copyToClipboard('{profile_obj.email}', this)",
                        ),
                        cls="bento-card",
                    ),
                    cls="bento-grid",
                ),
                cls="section",
            ),
        ),
    )
