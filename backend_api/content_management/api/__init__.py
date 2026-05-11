from backend_api.content_management.models.blog import Blog
from backend_api.content_management.models.contact import Contact
from backend_api.content_management.models.experience import Experience
from backend_api.content_management.models.home import Home
from backend_api.content_management.models.profile import Profile
from backend_api.content_management.models.project import Project
from backend_api.content_management.models.social import Social


def get_blogs():
    return Blog.select()


def get_contact():
    return Contact.select()[0]


def get_experiences():
    return Experience.select()


def get_home():
    return Home.select()[0]


def get_profile():
    return Profile.select()[0]


def get_projects():
    return Project.select()


def get_social():
    return Social.select()
