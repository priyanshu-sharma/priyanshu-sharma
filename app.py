from fastapi import FastAPI
from fasthtml.common import FastHTML, Meta, Style

from content import SITE
from pages import register_pages
from server_config.styles import CSS
from server_config import health_router

ui_app = FastHTML(
    title=SITE["title"],
    hdrs=(
        Meta(name="description", content=SITE["description"]),
        Meta(name="author", content=SITE["author"]),
        Meta(name="keywords", content=SITE["keywords"]),
        Meta(property="og:title", content=SITE["title"]),
        Meta(property="og:description", content=SITE["description"]),
        Meta(property="og:type", content="website"),
        Meta(name="theme-color", content="#000000"),
        Style(CSS),
    ),
)
register_pages(ui_app.route)

api_app = FastAPI(
    title=SITE["api_title"],
    description=SITE["api_description"],
    version=SITE["api_version"],
)
api_app.include_router(health_router)
ui_app.mount("/api", api_app)
app = ui_app
