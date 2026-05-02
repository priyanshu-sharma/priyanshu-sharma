from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fasthtml.common import FastHTML, Meta, Style, Link
from content import SITE
from backend.server_config.styles import CSS
from ui.pages import register_pages
from backend.server_config import health_router


def create_ui_app() -> FastHTML:
    """Creates and configures the main FastHTML application."""
    return FastHTML(
        title=SITE["title"],
        hdrs=(
            Meta(name="description", content=SITE["description"]),
            Meta(name="author", content=SITE["author"]),
            Meta(name="keywords", content=SITE["keywords"]),
            Meta(property="og:title", content=SITE["title"]),
            Meta(property="og:description", content=SITE["description"]),
            Meta(property="og:type", content="website"),
            Meta(name="theme-color", content="#000000"),
            Link(
                rel="stylesheet",
                href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
            ),
            Style(CSS),
        ),
    )


def create_api_app() -> FastAPI:
    """Creates and configures the FastAPI application."""
    api_app = FastAPI(
        title=SITE["api_title"],
        description=SITE["api_description"],
        version=SITE["api_version"],
    )
    api_app.include_router(health_router)
    return api_app


def create_app() -> FastHTML:
    """Composes and returns the final application."""
    ui_app = create_ui_app()
    api_app = create_api_app()

    register_pages(ui_app.route)

    ui_app.mount("/api", api_app)
    ui_app.mount("/static", StaticFiles(directory="static"), name="static")
    return ui_app


core_app = create_app()


@core_app.on_event("startup")
async def startup():
    print("--------------Starting The Application--------------")


@core_app.on_event("shutdown")
async def shutdown():
    print("--------------Closing The Application---------------")
