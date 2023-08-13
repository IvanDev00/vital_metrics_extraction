# Use an official Python runtime as a base image
FROM python:3.11.2-slim as builder

## Set the working directory in the container to /app
WORKDIR /app

# Copy only the requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install any needed packages specified in requirements.txt and compile them to wheels
RUN python -m pip install --upgrade pip \
    && pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# Final stage
FROM python:3.11.2-slim

# Create a non-root user
RUN useradd -m myuser
USER myuser

# Set the working directory in the container to /app
WORKDIR /app

# Copy the compiled wheels from the builder stage
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

# Install the Python packages from the wheels
RUN pip install --no-cache-dir /wheels/*

# Copy the rest of the application
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable for Flask to run in production mode
ENV FLASK_ENV=production

# Use gunicorn for production
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000", "--workers", "4"]