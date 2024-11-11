# Use a base image with Python and Jupyter Notebook
FROM jupyter/base-notebook:python-3.10.11

# Set the working directory in the container
WORKDIR /home/jovyan/work

# Copy the requirements file and install dependencies
COPY requirements.txt /home/jovyan/work/
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from your local folder into the container's work directory
COPY . .

# Expose the default Jupyter Notebook port
EXPOSE 8888

# Start both Python scripts in the background, and keep Jupyter Notebook running
CMD ["sh", "-c", "python parksim.py & python parksim_happyhour.py & jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root"]
