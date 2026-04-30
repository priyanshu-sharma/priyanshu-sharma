from fasthtml.common import *

from content import PROFILE

from .navigation import NAV_ITEMS


def page_shell(title: str, active_path: str, *content):
    nav_links = []
    for href, label in NAV_ITEMS:
        # Simplified navigation logic
        is_active = href == active_path
        cls = "btn btn-primary" if is_active else "btn"
        nav_links.append(A(label, href=href, cls=cls))

    return (
        Title(title),
        Div(
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
                    Script("""
                        function applyTheme(isDark) {
                            document.body.classList.toggle('light-mode', !isDark);
                            const themeToggle = document.querySelector('.theme-toggle');
                            if (themeToggle) themeToggle.innerText = isDark ? '🌙' : '☀️';
                            localStorage.setItem('theme', isDark ? 'dark' : 'light');
                        }
                        function toggleTheme() {
                            const isCurrentlyDark = !document.body.classList.contains('light-mode');
                            applyTheme(!isCurrentlyDark);
                        }
                        const savedTheme = localStorage.getItem('theme') || 'dark';
                        applyTheme(savedTheme === 'dark');
                    """),
                    cls="header-right",
                ),
                cls="header",
            ),
            Nav(Div(*nav_links, cls="nav"), cls="header-nav"),
            Main(*content),
            Footer(
                Div(
                    P(
                        PROFILE["availability"],
                        cls="muted",
                        style="margin:0; font-size:0.875rem;",
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
                    style="display:flex; flex-direction:column; gap:1rem;",
                ),
                cls="footer",
            ),
            cls="container",
        ),
    )
