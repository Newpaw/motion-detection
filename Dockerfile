# Use the latest official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install the necessary libraries and dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libgtk2.0-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir opencv-python ffmpeg-python

# Run the application
CMD ["python", "./motion_detection.py"]
