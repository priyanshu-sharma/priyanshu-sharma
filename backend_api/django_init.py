import os

import django
from django.conf import settings as django_settings


def setup_django():
    """Initializes the Django environment if not already configured."""
    if not django_settings.configured:
        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE", "backend_api.server_config.settings"
        )
        django.setup()
