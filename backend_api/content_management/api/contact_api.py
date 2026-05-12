from backend_api.content_management.models.contact import Contact
from databases.primary.content import contact


def get_contact() -> Contact:
    try:
        return Contact.select()[0]
    except Exception:
        return Contact(
            **{**contact.CONTACT, "created_by": "system", "updated_by": "system"}
        )
