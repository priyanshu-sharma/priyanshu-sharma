import os


def run() -> None:
    os.execvp(
        "gunicorn",
        [
            "gunicorn",
            "app:app",
            "-c",
            "server_config/gunicorn_conf.py",
        ],
    )


if __name__ == "__main__":
    run()
