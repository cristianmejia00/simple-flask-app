# Init from a Python base image
FROM python:3.9

# Define working directory within the container
WORKDIR /app

# Copy the contents of the folder where this Dockerfile is located to the container
# Files in the `.dockerignore` will be ignored
ADD . /app

# Install libraries
RUN apt-get update && apt-get install -y python3-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Define the command to start the container
CMD ["python3", "run.py"]