# Use the official Python base image
FROM python:3.10-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install application dependencies
RUN pip install --no-cache-dir  -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Run the application
ENTRYPOINT ["python", "/app/main.py"]