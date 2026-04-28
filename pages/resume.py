from fasthtml.common import *


def resume_page():
    return FileResponse("resume/resume.pdf")
