import os
from databases import db_migrate, load_fixtures


def run() -> None:
    load_fixtures()
    # Run database migrations before starting the application
    db_migrate()

    # Start the application
    os.execvp(
        "uv",
        [
            "uv",
            "run",
            "gunicorn",
            "core_app.app:core_app",
            "-c",
            "core_app/gunicorn_conf.py",
        ],
    )


if __name__ == "__main__":
    run()
