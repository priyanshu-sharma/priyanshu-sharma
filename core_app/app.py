from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fasthtml.common import FastHTML, Meta, Style, Link
from content import SITE
from backend_api.server_config.styles import CSS
from ui_design.pages import register_pages
from contextlib import asynccontextmanager
from backend_api.django_init import setup_django
from backend_api.server_config import health_router

# Path configuration
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"


async def lifespan(app: FastHTML):
    """Unified lifespan for both UI and API applications."""
    print("--------------🔥 Starting The UI Design--------------")
    async with api_app.router.lifespan_context(api_app):
        setup_django()
        yield
    print("--------------🛑 Closing The UI Design---------------")


def create_ui_app() -> FastHTML:
    """Creates and configures the main FastHTML application."""
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
        print("--------------🔥 Starting The Backend API--------------")
        yield
        print("--------------🛑 Closing The Backend API--------------")

    api_app = FastAPI(
        title=SITE["api_title"],
        description=SITE["api_description"],
        version=SITE["api_version"],
        lifespan=lifespan,
    )
    api_app.include_router(health_router)
    return api_app


# Initialize applications
api_app = create_api_app()


def create_app() -> FastHTML:
    """Composes and returns the final application."""
    ui_app = create_ui_app()
    register_pages(ui_app.route)

    ui_app.mount("/api", api_app)
    ui_app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

    return ui_app


core_app = create_app()
