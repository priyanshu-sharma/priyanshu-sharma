from fasthtml.common import *

from ui_design.components import page_shell
from backend_api.content_management.data import BLOG, PROFILE


def blog_page():
    posts = BLOG["posts"]
    return page_shell(
        f"Blog | {PROFILE['name']}",
        "/blog",
        Section(
            H2(BLOG["title"], cls="title"),
            P(BLOG["subtitle"], cls="subtitle muted"),
            cls="section",
        ),
        Section(
            *(
                (
                    Div(
                        Div(
                            H3(posts[i]["date"], style="margin: 0;"),
                            H4(
                                posts[i]["title"],
                                style="font-size: 1.7rem; margin: 0 0 0.5rem 0;",
                            ),
                            P(
                                posts[i]["summary"],
                                style="font-size: 1.1rem; margin: 0;",
                            ),
                            cls="bento-card",
                            style="flex: 7; gap: 0.25rem;",
                        ),
                        Div(
                            A(
                                "Read Post →",
                                href=posts[i]["href"],
                                cls="btn btn-primary",
                                style="padding: 1rem 1.5rem;",
                            ),
                            cls="bento-card",
                            style="flex: 3; justify-content: center; align-items: center;",
                        ),
                        style="display: flex; gap: 1.5rem; margin-bottom: 1.5rem;",
                    )
                    if i % 2 == 0
                    else Div(
                        Div(
                            A(
                                "Read Post →",
                                href=posts[i]["href"],
                                cls="btn btn-primary",
                                style="padding: 1rem 1.5rem;",
                            ),
                            cls="bento-card",
                            style="flex: 3; justify-content: center; align-items: center;",
                        ),
                        Div(
                            H3(posts[i]["date"], style="margin: 0;"),
                            H4(
                                posts[i]["title"],
                                style="font-size: 1.7rem; margin: 0 0 0.5rem 0;",
                            ),
                            P(
                                posts[i]["summary"],
                                style="font-size: 1.1rem; margin: 0;",
                            ),
                            cls="bento-card",
                            style="flex: 7; gap: 0.25rem;",
                        ),
                        style="display: flex; gap: 1.5rem; margin-bottom: 1.5rem;",
                    )
                )
                for i in range(len(posts))
            ),
            cls="section",
        ),
    )
