from fasthtml.common import A, Article, H3, H4, P, Div
from backend_api.content_management.models.project import Project


def project_card(project: Project):
    actions = []
    if project.demo_href:
        actions.append(
            A(
                "View Project →",
                href=project.demo_href,
                cls="btn btn-primary",
                target="_blank",
            )
        )
    return Article(
        H3(project.tag),
        H4(project.title),
        P(project.desc),
        Div(*actions, cls="btn-row") if actions else None,
        cls="card",
    )
