from fasthtml.common import *

from ui.components import page_shell
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
            Div(
                # Top Row: Me, Experience, Resume
                Div(
                    Div(H3("Me"), P("Priyanshu Sharma 👋"), cls="bento-card"),
                    Div(H3("Experience"), P("7+ Years"), cls="bento-card"),
                    Div(
                        H3("Resume"),
                        A(
                            "View PDF",
                            href=PROFILE["resume_path"],
                            cls="btn btn-primary",
                        ),
                        cls="bento-card",
                    ),
                    cls="top-row",
                ),
                # Philosophy (Full Width)
                Div(
                    H3("Philosophy"),
                    P(HOME["philosophy"]),
                    cls="bento-card",
                    style="margin-bottom: 1.5rem;",
                ),
                # Toolkit & Workspace (Shared Width)
                Div(
                    Div(
                        H3("Toolkit"),
                        P(
                            "Python, Spark, Airflow, Kafka, dbt, Snowflake, Kubernetes, AWS, GCP."
                        ),
                        cls="bento-card",
                        style="flex: 1;",
                    ),
                    Div(
                        H3("Workspace"),
                        P(HOME["setup"]),
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
                        P(HOME["learning"]),
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
                        A(
                            "Email Me",
                            href=f"mailto:{PROFILE['email']}",
                            cls="btn btn-primary",
                        ),
                        cls="bento-card",
                    ),
                    cls="bento-grid",
                ),
                cls="section",
            ),
        ),
    )
