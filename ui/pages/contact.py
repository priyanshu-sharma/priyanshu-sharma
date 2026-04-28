from fasthtml.common import *

from ui.components import page_shell
from content import CONTACT, PROFILE


def contact_page():
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
