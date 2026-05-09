import os
import subprocess


def run() -> None:
    # Run migrations
    subprocess.run(["uv", "run", "python", "manage.py", "migrate"], check=True)

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
