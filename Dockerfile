# Use an official Python runtime as a base image
FROM python:3.11.4-slim-bullseye AS build

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Now, create a new build stage to minimize the final image size
FROM python:3.11.4-slim-bullseye

# Metadata as described above
LABEL maintainer="ivandev00" \
      version="1.0"

# Set the working directory in the container to /app
WORKDIR /app

RUN apt-get update && apt-get install -y \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Copy over the files from the build stage above, as well as the other necessary files
COPY --from=build /app /app

COPY . .

# Inform Docker that the container is listening on the specified port at runtime.
EXPOSE 80

# Starting Nginx and Gunicorn
CMD ["gunicorn","--config", "gunicorn_config.py", "app:app"]
