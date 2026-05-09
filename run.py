import os
from databases.db_migrate import db_migrate


def run() -> None:
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
