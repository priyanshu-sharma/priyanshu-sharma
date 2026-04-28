from fasthtml.common import FastHTML, Style
from fastapi import FastAPI
from pages import register_pages
from server_config.styles import CSS
from server_config import health_router

ui_app = FastHTML(hdrs=(Style(CSS),))
register_pages(ui_app.route)
api_app = FastAPI()
api_app.include_router(health_router)
ui_app.mount("/api", api_app)
app = ui_app
