from typing import List
from backend_api.content_management.models.blog import Blog
from backend_api.content_management.models.contact import Contact
from backend_api.content_management.models.experience import Experience
from backend_api.content_management.models.home import Home
from backend_api.content_management.models.profile import Profile
from backend_api.content_management.models.project import Project
from backend_api.content_management.models.social import Social

# Import original static data for fallback
from databases.primary.content import (
    blog,
    contact,
    experience,
    home,
    profile,
    projects,
    social,
)


def get_blogs() -> List[Blog]:
    try:
        return Blog.select()
    except Exception:
        # Fallback to static data
        return [
            Blog(**{**post, "created_by": "fallback", "updated_by": "fallback"})
            for post in blog.BLOG["posts"]
        ]


def get_contact() -> Contact:
    try:
        return Contact.select()[0]
    except Exception:
        return Contact(
            **{**contact.CONTACT, "created_by": "fallback", "updated_by": "fallback"}
        )


def get_experiences() -> List[Experience]:
    try:
        return Experience.select()
    except Exception:
        return [
            Experience(**{**role, "created_by": "fallback", "updated_by": "fallback"})
            for role in experience.EXPERIENCE["roles"]
        ]


def get_home() -> Home:
    try:
        return Home.select()[0]
    except Exception:
        return Home(**{**home.HOME, "created_by": "fallback", "updated_by": "fallback"})


def get_profile() -> Profile:
    try:
        return Profile.select()[0]
    except Exception:
        return Profile(
            **{**profile.PROFILE, "created_by": "fallback", "updated_by": "fallback"}
        )


def get_projects() -> List[Project]:
    try:
        return Project.select()
    except Exception:
        return [
            Project(**{**item, "created_by": "fallback", "updated_by": "fallback"})
            for item in projects.PROJECTS["items"]
        ]


def get_social() -> List[Social]:
    try:
        return Social.select()
    except Exception:
        return [
            Social(**{**link, "created_by": "fallback", "updated_by": "fallback"})
            for link in social.SOCIAL["links"]
        ]
