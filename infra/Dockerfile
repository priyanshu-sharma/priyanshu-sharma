FROM python:3.14-slim

WORKDIR /app

# Install dependencies
RUN pip install uv
COPY pyproject.toml uv.lock ./
RUN uv sync

COPY . .

# Run the app
CMD ["python", "run.py"]
