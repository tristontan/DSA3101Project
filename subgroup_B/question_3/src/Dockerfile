# Use a base Python image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Install GLPK
RUN apt-get update && apt-get install -y glpk-utils

# Copy project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the Flask app will run on
EXPOSE 5001

# Command to start the Flask API
CMD ["python", "DSA3101_Project_Question B3.py"]
