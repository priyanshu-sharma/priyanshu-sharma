from fasthtml.common import Div, H2, H3, P, Section
from ui_design.components import page_shell, project_card
from backend_api.content_management.api import get_profile
from backend_api.content_management.models.project import Project


def gallery_page():
    profile_obj = get_profile()
    sample_project = Project(
        tag="Gallery Sample",
        title="Sample Project",
        desc="This is a sample project card used for component gallery purposes.",
        demo_href="#",
        created_by="system",
        updated_by="system",
    )

    return page_shell(
        f"Gallery | {profile_obj.name}",
        "/gallery",
        Section(
            H2("Component Gallery", cls="title"),
            P(
                "Isolated preview of UI components for consistent design.",
                cls="subtitle muted",
            ),
            cls="section",
        ),
        Section(
            H3("Project Card"),
            Div(project_card(sample_project), style="max-width: 400px;"),
            cls="section",
        ),
    )
