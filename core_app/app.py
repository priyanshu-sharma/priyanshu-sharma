from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fasthtml.common import FastHTML, Meta, Style, Link
from backend_api.content_management.data import SITE
from backend_api.server_config.styles import CSS
from ui_design.pages import register_pages
from backend_api.server_config.env_settings import settings

from contextlib import asynccontextmanager
from backend_api.django_init import setup_django
from backend_api.server_config import health_router

# Path configuration
STATIC_DIR = settings.project_root / "ui_design" / "static"


def create_ui_app(api_app: FastAPI) -> FastHTML:
    """Creates and configures the main FastHTML application."""

    async def lifespan(app: FastHTML):
        """Unified lifespan for both UI and API applications."""
        print("--------------🔥 Starting The UI Design--------------")
        setup_django()
        yield
        print("--------------🛑 Closing The UI Design---------------")

    return FastHTML(
        title=SITE["title"],
        lifespan=lifespan,
        hdrs=(
            Meta(name="description", content=SITE["description"]),
            Meta(name="author", content=SITE["author"]),
            Meta(name="keywords", content=SITE["keywords"]),
            Meta(property="og:title", content=SITE["title"]),
            Meta(property="og:description", content=SITE["description"]),
            Meta(property="og:image", content=f"{SITE['url']}/static/og-image.png"),
            Meta(property="og:url", content=SITE["url"]),
            Meta(property="og:type", content="website"),
            Meta(name="twitter:card", content="summary_large_image"),
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

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        print(
            f"--------------🔥 Starting The Backend API (Debug={settings.debug})--------------"
        )
        yield
        print("--------------🛑 Closing The Backend API---------------")

    api_app = FastAPI(
        title=SITE["api_title"],
        description=SITE["api_description"],
        version=SITE["api_version"],
        lifespan=lifespan,
        debug=settings.debug,
    )
    api_app.include_router(health_router)
    return api_app


def create_app() -> FastHTML:
    """Composes and returns the final application."""
    api_app = create_api_app()
    ui_app = create_ui_app(api_app)

    register_pages(ui_app.route)

    ui_app.mount("/api", api_app)
    ui_app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

    return ui_app


core_app = create_app()
