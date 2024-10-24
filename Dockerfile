# Use python:3.9-slim as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application code into the Docker image
COPY . /app

# Install the required dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Set the entry point to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
