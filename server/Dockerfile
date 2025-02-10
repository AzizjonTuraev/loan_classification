# Use an official Python runtime as the base image
FROM python:3.11.5

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .
# Expose the port your Flask app will run on
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "server.py"]


#### Commands to run the docker file
# docker build -t my_flask_app .
# docker run -p 5000:5000 my_flask_app