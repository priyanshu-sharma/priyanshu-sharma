from fasthtml.common import FileResponse


def resume_page():
    return FileResponse("backend/resume/resume.pdf")
