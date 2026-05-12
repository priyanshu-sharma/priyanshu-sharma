from backend_api.content_management.models.blog import Blog
from backend_api.content_management.models.contact import Contact
from backend_api.content_management.models.experience import Experience
from backend_api.content_management.models.home import Home
from backend_api.content_management.models.profile import Profile
from backend_api.content_management.models.project import Project
from backend_api.content_management.models.social import Social
from databases.primary.content import (
    blog,
    contact,
    experience,
    home,
    profile,
    projects,
    social,
)


def test_blog_data():
    for post in blog.BLOG["posts"]:
        post.update({"created_by": "test", "updated_by": "test"})
        assert Blog(**post)


def test_contact_data():
    data = contact.CONTACT.copy()
    data.update({"created_by": "test", "updated_by": "test"})
    assert Contact(**data)


def test_experience_data():
    for role in experience.EXPERIENCE["roles"]:
        role.update({"created_by": "test", "updated_by": "test"})
        assert Experience(**role)


def test_home_data():
    data = home.HOME.copy()
    data.update({"created_by": "test", "updated_by": "test"})
    assert Home(**data)


def test_profile_data():
    data = profile.PROFILE.copy()
    data.update({"created_by": "test", "updated_by": "test"})
    assert Profile(**data)


def test_projects_data():
    for item in projects.PROJECTS["items"]:
        item.update({"created_by": "test", "updated_by": "test"})
        assert Project(**item)


def test_social_data():
    for link in social.SOCIAL["links"]:
        link.update({"created_by": "test", "updated_by": "test"})
        assert Social(**link)
