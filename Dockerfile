# Use the specified Python image
FROM python:3.11.2-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Update and install necessary packages
RUN apt-get update && \
    apt-get install -y libgl1-mesa-dev ffmpeg libsm6 libxext6 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn
RUN pip install --no-cache-dir gunicorn

# Copy the content of the local src directory to the working directory
COPY . .

# Specify the command to run on container start
CMD ["gunicorn", "app:app", "-w 4", "-b 0.0.0.0:8000", "--reload"]



# # Use an official Python runtime as a base image
# FROM python:3.11.2-slim as builder

# # Set the working directory in the container to /app
# WORKDIR /app

# # Copy only the requirements.txt first to leverage Docker cache
# COPY requirements.txt .

# # Install any needed packages specified in requirements.txt and compile them to wheels
# RUN apt-get update && apt-get install -y \
#     libgl1-mesa-dev \
#     && python -m pip install --upgrade pip \
#     && pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# # Final stage
# FROM python:3.11.2-slim

# # Install the necessary system libraries for OpenCV
# RUN apt-get update && apt-get install -y \
#     libgl1-mesa-glx

# # Create a non-root user
# RUN useradd -m myuser

# # Set the working directory in the container to /app
# WORKDIR /app

# # Copy the compiled wheels from the builder stage
# COPY --from=builder /app/wheels /wheels
# COPY --from=builder /app/requirements.txt .

# # Install the Python packages from the wheels
# RUN pip install --no-cache-dir /wheels/*

# # Switch to the non-root user
# USER myuser

# # Copy the rest of the application
# COPY . .

# # Make port 5000 available to the world outside this container
# EXPOSE 5000

# # Define environment variable for Flask to run in production mode
# ENV FLASK_ENV=production

# # Use gunicorn for production in shell form
# CMD gunicorn app:app --bind 0.0.0.0:5000 --workers 4
