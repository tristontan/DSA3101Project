# Linear Programming Optimization Model

This project provides a Dockerized Flask API for a linear programming optimization model implemented in Python. The API is designed to handle requests and return optimized staff allocations and wait times based on specified input dates.

## Project Structure

- **`DSA3101_Project_Question B3.py`**: Python script containing the main code for the linear programming optimization model and Flask API.
- **`requirements.txt`**: List of dependencies required to run the application.
- **`test_api.py`**: Script to test the API by sending requests to the endpoint and displaying the responses.
- **`Dockerfile`**: Docker configuration file for containerizing the application.
- **`README.md`**: Documentation for setup and usage instructions.

## Prerequisites

Before setting up the project, ensure you have the following installed:

1. **Docker**: [Install Docker](https://docs.docker.com/get-docker/) on your system.
2. **Python 3.x**: Install Python to run the test script (`test_api.py`) outside Docker if needed.

## Setup and Installation

### 1. Clone the Repository

### 2. Build the Docker Image
Run the following command to build the Docker image:
```bash
docker build -t my-flask-api .
```
This command will create a Docker image named `my-flask-api`.

### 3. Run the Docker Container
To start the container and make the API accessible on your local machine, use:
```bash
docker run -p 5001:5001 my-flask-api
```
This maps port 5001 on your host to port 5001 in the container, allowing you to access the API at `http://127.0.0.1:5001`.

## Testing the API
You can test the API using the provided `test_api.py` script.
Make sure the container is running, then in another terminal, run:
```bash
python3 test_api.py
```
The `test_api.py` script sends a test request to the API and prints the response.
