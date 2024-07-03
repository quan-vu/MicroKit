# Step 1: Create a Dockerfile for your FastAPI application
# Dockerfile
FROM python:3.8-slim-buster

WORKDIR /app

COPY pyproject.toml .

RUN pip install poetry && poetry config virtualenvs.create false && poetry install

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]