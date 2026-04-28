from fasthtml.common import *

from content import PROFILE

from .navigation import NAV_ITEMS


def page_shell(title: str, active_path: str, *content):
    nav_links = []
    for href, label in NAV_ITEMS:
        cls = "btn btn-primary" if href == active_path else "btn"
        nav_links.append(A(label, href=href, cls=cls))

    return (
        Title(title),
        Div(
            Header(
                Div(Div(cls="avatar"), cls="header-left"),
                Div(H1(PROFILE["name"], cls="h1"), cls="header-center"),
                Div(
                    Button("🌙", cls="theme-toggle", onclick="toggleTheme()"),
                    Script("""
                        function applyTheme(isDark) {
                            document.body.classList.toggle('light-mode', !isDark);
                            document.querySelector('.theme-toggle').innerText = isDark ? '🌙' : '☀️';
                            localStorage.setItem('theme', isDark ? 'dark' : 'light');
                        }
                        function toggleTheme() {
                            const isDark = document.body.classList.contains('light-mode');
                            applyTheme(isDark);
                        }
                        const savedTheme = localStorage.getItem('theme') || 'dark';
                        applyTheme(savedTheme === 'dark');
                    """),
                    cls="header-right",
                ),
                cls="header",
            ),
            Nav(Div(*nav_links, cls="nav"), cls="header-nav"),
            *content,
            Footer(
                P(PROFILE["availability"], cls="muted", style="margin:0;"),
                Div(
                    A("Email", href=f"mailto:{PROFILE['email']}", cls="btn"),
                    A("Resume", href=PROFILE["resume_path"], cls="btn"),
                    cls="btn-row",
                ),
                cls="footer",
            ),
            cls="container",
        ),
    )
