from .blog import blog_page
from .contact import contact_page
from .experience import experience_page
from .home import home_page
from .projects import projects_page
from .resume import resume_page
from .social import social_page


def register_pages(rt):
    @rt("/")
    def home():
        return home_page()

    @rt("/projects")
    def projects():
        return projects_page()

    @rt("/experience")
    def experience():
        return experience_page()

    @rt("/contact")
    def contact():
        return contact_page()

    @rt("/blog")
    def blog():
        return blog_page()

    @rt("/social")
    def social():
        return social_page()

    @rt("/resume")
    def resume():
        return resume_page()
