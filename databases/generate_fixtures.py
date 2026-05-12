import json
from datetime import datetime
from pathlib import Path
from uuid import uuid4

from backend_api.content_management.models.blog import Blog
from backend_api.content_management.models.contact import Contact
from backend_api.content_management.models.experience import Experience
from backend_api.content_management.models.home import Home
from backend_api.content_management.models.profile import Profile
from backend_api.content_management.models.project import Project
from backend_api.content_management.models.site import Site
from backend_api.content_management.models.social import Social
from databases.primary.content import (
    blog,
    contact,
    experience,
    home,
    profile,
    projects,
    site,
    social,
)

FIXTURES_DIR = Path("databases/primary/fixtures")
FIXTURES_DIR.mkdir(parents=True, exist_ok=True)


def generate_item(model, data):
    # Add default system fields
    if "uuid" not in data:
        data["uuid"] = uuid4().hex
    if "active" not in data:
        data["active"] = True
    data["created_by"] = "system"
    data["updated_by"] = "system"
    now = datetime.now().isoformat()
    data["install_ts"] = now
    data["update_ts"] = now

    # Validate with Pydantic model
    instance = model(**data)
    return instance.model_dump()


def save_fixture(filename, data):
    with open(FIXTURES_DIR / filename, "w") as f:
        json.dump(data, f, indent=2, default=str)
    print(f"Generated {filename}")


def run():
    # Blog
    blog_data = [generate_item(Blog, post) for post in blog.BLOG["posts"]]
    save_fixture("blog.json", blog_data)

    # Contact
    save_fixture("contact.json", [generate_item(Contact, contact.CONTACT)])

    # Experience
    exp_data = [
        generate_item(Experience, role) for role in experience.EXPERIENCE["roles"]
    ]
    save_fixture("experiences.json", exp_data)

    # Home
    save_fixture("home.json", [generate_item(Home, home.HOME)])

    # Profile
    save_fixture("profile.json", [generate_item(Profile, profile.PROFILE)])

    # Projects
    proj_data = [generate_item(Project, item) for item in projects.PROJECTS["items"]]
    save_fixture("projects.json", proj_data)

    # Site
    save_fixture("site.json", [generate_item(Site, site.SITE)])

    # Social
    social_data = [generate_item(Social, link) for link in social.SOCIAL["links"]]
    save_fixture("social.json", social_data)


if __name__ == "__main__":
    run()
