from fasthtml.common import *


def resume_page():
    return FileResponse("backend/resume/resume.pdf")
