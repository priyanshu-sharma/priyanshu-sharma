from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fasthtml.common import FastHTML, Meta, Style, Link
from contextlib import asynccontextmanager
from backend_api.content_management.data import SITE
from backend_api.server_config.styles import CSS
from backend_api.server_config.env_settings import settings
from backend_api.server_config import health_router
from backend_api.django_init import setup_django
from databases.db_migrate import db_migrate
from ui_design.pages import register_pages

STATIC_DIR = settings.project_root / "ui_design" / "static"


@asynccontextmanager
async def api_lifespan(app: FastAPI):
    print("-----------------🔥 Starting Backend API-----------------")
    setup_django()
    db_migrate()
    yield
    print("-----------------🛑 Closing Backend API------------------")


def create_api_app() -> FastAPI:
    api_app = FastAPI(
        title=SITE["api_title"],
        description=SITE["api_description"],
        version=SITE["api_version"],
        lifespan=api_lifespan,
        debug=settings.debug,
    )
    api_app.include_router(health_router)
    return api_app


async def ui_lifespan(app: FastHTML):
    print("-----------------🔥 Starting UI Design-----------------")

    async with api_lifespan(app):
        yield

    print("-----------------🛑 Closing UI Design------------------")


def create_ui_app(api_app: FastAPI) -> FastHTML:
    ui_app = FastHTML(
        title=SITE["title"],
        lifespan=ui_lifespan,
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
    register_pages(ui_app.route)
    ui_app.mount("/api", api_app)
    ui_app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

    return ui_app


def create_app() -> FastHTML:
    api_app = create_api_app()
    ui_app = create_ui_app(api_app)
    return ui_app


core_app = create_app()
