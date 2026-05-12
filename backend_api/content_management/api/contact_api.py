from backend_api.content_management.models.contact import Contact
from databases.primary.content import contact


def get_contact() -> Contact:
    try:
        data = Contact.select()
        if data:
            return data[0]
        raise Exception("No contact found")
    except Exception:
        return Contact(
            **{**contact.CONTACT, "created_by": "system", "updated_by": "system"}
        )
