# Use an official Python image from the Docker Hub as the base
FROM python:3.9-slim

# Set a working directory for the app
WORKDIR /app

# Copy requirements.txt file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . /app

# Expose the port Flask will run on (default is 5000)
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
