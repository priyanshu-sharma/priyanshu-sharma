from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fasthtml.common import FastHTML, Meta, Style, Link
from contextlib import asynccontextmanager
from databases.primary.content import SITE
from backend_api.server_config.styles import CSS
from backend_api.server_config.settings import DEBUG, STATIC_DIR
from backend_api.server_config import health_router
from backend_api.django_init import setup_django
from ui_design.pages import register_pages
from databases.init_redis import verify_redis, clear_redis

import time
from fastapi import Request
from backend_api.server_config.logging import setup_logging
import structlog

log = structlog.get_logger()


# Middleware for request latency
@asynccontextmanager
async def api_lifespan(app: FastAPI):
    setup_logging()
    log.info("starting_backend_api")
    verify_redis()
    setup_django()
    yield
    clear_redis()
    log.info("closing_backend_api")


def create_api_app() -> FastAPI:
    api_app = FastAPI(
        title=SITE["api_title"],
        description=SITE["api_description"],
        version=SITE["api_version"],
        lifespan=api_lifespan,
        debug=DEBUG,
    )
    api_app.include_router(health_router)

    @api_app.middleware("http")
    async def log_requests(request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time
        log.info(
            "http_request",
            method=request.method,
            path=request.url.path,
            duration=f"{duration:.4f}s",
            status_code=response.status_code,
        )
        return response

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
