# Use an official Python runtime as a base image
FROM python:3.8-slim as builder

# Set the working directory in the container to /app
WORKDIR /app

# Copy only the requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Start a new stage
FROM python:3.8-slim

# Create a non-root user
RUN useradd -m myuser
USER myuser

# Set the working directory in the container to /app
WORKDIR /app

# Copy from the builder stage
COPY --from=builder /app /app
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable for Flask to run in production mode
ENV FLASK_ENV=production

# Use gunicorn for production
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000", "--workers", "4"]
