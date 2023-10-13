FROM python:3.11.4-slim-bullseye AS build
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11.4-slim-bullseye  
LABEL maintainer="ivandev00"
LABEL version="1.0" 
WORKDIR /app
RUN apt-get update && apt-get install -y poppler-utils && rm -rf /var/lib/apt/lists/* && apt-get clean
COPY --from=build /app /app 
COPY . .
EXPOSE 80
HEALTHCHECK CMD curl --fail http://localhost/healthz || exit 1  
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "app:app"]