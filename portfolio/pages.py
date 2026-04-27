from fasthtml.common import *

from components import metric_card, page_shell, project_card
from content import BLOG, CONTACT, EXPERIENCE, HOME, PROFILE, PROJECTS, SOCIAL


def register_pages(rt):
    @rt("/")
    def home():
        return page_shell(
            f"{PROFILE['name']} | {PROFILE['role']}",
            "/",
            Section(
                H2(HOME["title"], cls="title"),
                P(HOME["subtitle"], cls="subtitle muted"),
                Div(*(Span(item, cls="badge") for item in HOME["badges"]), cls="badge-row"),
                cls="section card",
            ),
            Section(
                H3(HOME["snapshot_title"], cls="section-label"),
                Div(
                    *(metric_card(metric["value"], metric["label"]) for metric in HOME["metrics"]),
                    cls="metric-grid",
                ),
                cls="section card",
            ),
        )

    @rt("/projects")
    def projects():
        return page_shell(
            f"Projects | {PROFILE['name']}",
            "/projects",
            Section(
                H2(PROJECTS["title"], cls="title"),
                P(PROJECTS["subtitle"], cls="subtitle muted"),
                cls="section",
            ),
            Section(
                Div(
                    *(
                        project_card(item["tag"], item["title"], item["desc"])
                        for item in PROJECTS["items"]
                    ),
                    cls="grid-2",
                ),
                cls="section",
            ),
        )

    @rt("/experience")
    def experience():
        return page_shell(
            f"Experience | {PROFILE['name']}",
            "/experience",
            Section(
                H2(EXPERIENCE["title"], cls="title"),
                P(EXPERIENCE["subtitle"], cls="subtitle muted"),
                cls="section",
            ),
            Section(
                Div(
                    *(
                        Article(
                            H3(role["title"], cls="section-label"),
                            P(role["summary"], cls="muted"),
                            P(role["details"], style="margin-top:0.6rem;"),
                            cls="card",
                        )
                        for role in EXPERIENCE["roles"]
                    ),
                    cls="grid-2",
                ),
                cls="section",
            ),
        )

    @rt("/contact")
    def contact():
        return page_shell(
            f"Contact | {PROFILE['name']}",
            "/contact",
            Section(
                H2(CONTACT["title"], cls="title"),
                P(CONTACT["subtitle"], cls="subtitle muted"),
                Div(
                    A("Email Me", href=f"mailto:{PROFILE['email']}", cls="btn btn-primary"),
                    A("Download Resume", href=PROFILE["resume_path"], cls="btn"),
                    cls="btn-row",
                ),
                cls="section card",
            ),
        )

    @rt("/blog")
    def blog():
        return page_shell(
            f"Blog | {PROFILE['name']}",
            "/blog",
            Section(
                H2(BLOG["title"], cls="title"),
                P(BLOG["subtitle"], cls="subtitle muted"),
                cls="section",
            ),
            Section(
                Div(
                    *(
                        Article(
                            P(post["date"], cls="muted", style="margin:0 0 0.35rem;font-size:0.78rem;"),
                            H3(post["title"], cls="section-label"),
                            P(post["summary"], cls="muted"),
                            A("Read Post", href=post["href"], cls="btn", style="margin-top:0.8rem;"),
                            cls="card",
                        )
                        for post in BLOG["posts"]
                    ),
                    cls="grid-2",
                ),
                cls="section",
            ),
        )

    @rt("/social")
    def social():
        return page_shell(
            f"Social | {PROFILE['name']}",
            "/social",
            Section(
                H2(SOCIAL["title"], cls="title"),
                P(SOCIAL["subtitle"], cls="subtitle muted"),
                cls="section",
            ),
            Section(
                Div(
                    *(
                        Article(
                            H3(item["name"], cls="section-label"),
                            P(item["description"], cls="muted"),
                            A(item["cta"], href=item["href"], cls="btn", style="margin-top:0.8rem;"),
                            cls="card",
                        )
                        for item in SOCIAL["links"]
                    ),
                    cls="grid-2",
                ),
                cls="section",
            ),
        )

    @rt("/resume")
    def resume():
        return FileResponse("../resume/resume.pdf")
