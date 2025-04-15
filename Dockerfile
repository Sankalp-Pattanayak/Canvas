# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt to the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --default-timeout=300 --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /app/

# Expose the port your app runs on
EXPOSE 5000

# Set the environment variable for Flask to run in production mode
ENV FLASK_APP=main.py
ENV FLASK_ENV=production

# Command to run the application
CMD ["python", "main.py"]
