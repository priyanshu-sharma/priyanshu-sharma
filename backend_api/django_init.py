import os
import django


def setup_django():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "backend_api.server_config.settings"
    )
    django.setup()
