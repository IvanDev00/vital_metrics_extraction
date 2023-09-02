# ---- Base Python ----
FROM python:3.11.2-slim AS base
WORKDIR /app
RUN apt-get update && apt-get install -y poppler-utils && apt-get clean && rm -rf /var/lib/apt/lists/*

# ---- Dependencies ----
FROM base AS dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# ---- Copy Files/Build ----
FROM dependencies AS build
COPY . /app

# ---- Production Image ----
FROM base AS release
COPY --from=build /usr/local /usr/local
COPY --from=build /app /app
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]