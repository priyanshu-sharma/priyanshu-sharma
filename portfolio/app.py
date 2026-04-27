from fasthtml.common import *

from pages import register_pages
from styles import CSS

app, rt = fast_app(hdrs=(Style(CSS),))
register_pages(rt)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=4173, reload=True)
