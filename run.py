import os


def run() -> None:
    os.execvp(
        "gunicorn",
        [
            "gunicorn",
            "core_app.app:core_app",
            "-c",
            "core_app/gunicorn_conf.py",
        ],
    )


if __name__ == "__main__":
    run()
