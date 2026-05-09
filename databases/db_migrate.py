import subprocess


def db_migrate() -> None:
    subprocess.run(["uv", "run", "python", "manage.py", "migrate"], check=True)
