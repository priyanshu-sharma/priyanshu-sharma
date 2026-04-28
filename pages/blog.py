from fasthtml.common import *

from components import page_shell
from content import BLOG, PROFILE


def blog_page():
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
                        P(
                            post["date"],
                            cls="muted",
                            style="margin:0 0 0.35rem;font-size:0.78rem;",
                        ),
                        H3(post["title"], cls="section-label"),
                        P(post["summary"], cls="muted"),
                        A(
                            "Read Post",
                            href=post["href"],
                            cls="btn",
                            style="margin-top:0.8rem;",
                        ),
                        cls="card",
                    )
                    for post in BLOG["posts"]
                ),
                cls="grid-2",
            ),
            cls="section",
        ),
    )
