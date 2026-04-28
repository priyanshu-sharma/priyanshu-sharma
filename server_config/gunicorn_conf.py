import multiprocessing

bind = "127.0.0.1:4000"
worker_class = "uvicorn.workers.UvicornWorker"
reload = True

# Keep at least 4 workers, scale up on larger machines.
workers = max(4, multiprocessing.cpu_count())

# Emit logs to console with info-level verbosity.
loglevel = "info"
accesslog = "-"
errorlog = "-"
capture_output = True
