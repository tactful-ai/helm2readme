# Use a minimal Alpine Linux as the base image
FROM python:3.9-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY ./requirements* /app

# Install any Python dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . /app

# Define the command to run your application
ENTRYPOINT ["python", "main.py"]
