# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8888 to allow Jupyter notebook access
EXPOSE 8888

# Command to run Jupyter notebook server
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root"]