from fasthtml.common import *

from content import PROFILE

NAV_ITEMS = [
    ("/", "Home"),
    ("/projects", "Projects"),
    ("/products", "Products"),
    ("/experience", "Experience"),
    ("/blog", "Blog"),
    ("/social", "Social"),
    ("/contact", "Contact"),
]


def page_shell(title: str, active_path: str, *content):
    nav_links = []
    for href, label in NAV_ITEMS:
        # Simplified navigation logic
        is_active = href == active_path
        cls = "btn btn-primary" if is_active else "btn"
        attrs = {"aria-current": "page"} if is_active else {}
        nav_links.append(A(label, href=href, cls=cls, **attrs))

    return (
        Title(title),
        Div(
            Div(Div(cls="blob blob-1"), Div(cls="blob blob-2"), cls="bg-blobs"),
            Header(
                Div(
                    A(Div(cls="avatar"), href="/"),
                    H1(PROFILE["name"], cls="h1"),
                    cls="header-left",
                    style="display:flex; align-items:center; gap:1rem;",
                ),
                Div(
                    Button(
                        "🌙",
                        cls="theme-toggle",
                        onclick="toggleTheme()",
                        aria_label="Toggle theme",
                    ),
                    Script(src="/static/js/theme.js"),
                    Script("""
                        function copyToClipboard(text, btn) {
                            navigator.clipboard.writeText(text);
                            const originalText = btn.innerText;
                            btn.innerText = '✓ Copied!';
                            setTimeout(() => btn.innerText = originalText, 2000);
                        }
                    """),
                    cls="header-right",
                    style="display:flex; align-items:center; gap:1rem;",
                ),
                cls="header",
                style="display:flex; align-items:center; justify-content:space-between; padding: 1rem 0;",
            ),
            Nav(Div(*nav_links, cls="nav"), cls="header-nav"),
            Main(*content),
            Footer(
                Div(
                    P(
                        PROFILE["availability"],
                        cls="muted",
                    ),
                    Div(
                        A(
                            "Email",
                            href=f"mailto:{PROFILE['email']}",
                            cls="btn btn-primary",
                        ),
                        A("Resume", href=PROFILE["resume_path"], cls="btn btn-primary"),
                        cls="btn-row",
                    ),
                ),
                cls="footer",
            ),
            cls="container",
        ),
    )
