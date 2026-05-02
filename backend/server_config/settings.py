import multiprocessing

# Gunicorn configuration settings
BIND_HOST = "127.0.0.1"
BIND_PORT = 4000
BIND = f"{BIND_HOST}:{BIND_PORT}"
WORKER_CLASS = "uvicorn.workers.UvicornWorker"
RELOAD = False
MIN_WORKERS = 4
WORKERS = min(MIN_WORKERS, multiprocessing.cpu_count())
LOG_LEVEL = "info"
ACCESS_LOG = "-"
ERROR_LOG = "-"
CAPTURE_OUTPUT = False
