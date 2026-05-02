from .blog import blog_page
from .contact import contact_page
from .experience import experience_page
from .home import home_page
from .projects import projects_page
from .products import products_page
from .resume import resume_page
from .social import social_page


def register_pages(rt):
    routes = {
        "/": home_page,
        "/projects": projects_page,
        "/products": products_page,
        "/experience": experience_page,
        "/contact": contact_page,
        "/blog": blog_page,
        "/social": social_page,
        "/resume": resume_page,
    }
    for path, func in routes.items():
        rt(path)(func)
