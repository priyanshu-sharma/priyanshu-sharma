from fasthtml.common import *

from ui_design.components import page_shell
from backend_api.content_management.models.contact import Contact
from backend_api.content_management.models.profile import Profile


def contact_page():
    contact_obj = Contact.select()[0]
    profile_obj = Profile.select()[0]

    return page_shell(
        f"Contact | {profile_obj.name}",
        "/contact",
        Section(
            H2(contact_obj.title, cls="title"),
            P(
                "Let's connect for opportunities, consulting, or technical discussions.",
                cls="subtitle muted",
            ),
            cls="section",
        ),
        Section(
            Div(
                # Me Card
                Div(
                    H3("About"),
                    H4("Me"),
                    P(f"{profile_obj.name} 👋"),
                    cls="card",
                ),
                # Now Card
                Div(
                    H3("Activity"),
                    H4("Now"),
                    P(
                        "Deepening my understanding of Rust and building scalable data platforms."
                    ),
                    cls="card",
                ),
                Div(
                    H3("Contact Details"),
                    H4("Phone"),
                    P("+1 (858)-305-8168", style="margin-bottom: 1.5rem;"),
                    Button(
                        "Copy",
                        cls="btn btn-primary",
                        onclick="copyToClipboard('+1 (858)-305-8168', this)",
                    ),
                    style="display:flex; flex-direction:column; align-items:start;",
                    cls="card",
                ),
                Div(
                    H3("Contact Details"),
                    H4("Location"),
                    P("New York City, NY"),
                    A(
                        "View Map",
                        href="https://www.google.com/maps/place/New+York,+NY",
                        cls="btn btn-primary",
                        style="margin-top: 0.5rem;",
                    ),
                    cls="card",
                ),
                style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;",
            ),
            cls="section",
        ),
    )
