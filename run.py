import os


def run() -> None:
    os.execvp(
        "gunicorn",
        [
            "gunicorn",
            "core.app:core_app",
            "-c",
            "backend/server_config/gunicorn_conf.py",
        ],
    )


if __name__ == "__main__":
    run()
