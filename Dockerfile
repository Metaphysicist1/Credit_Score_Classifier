# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Install PostgreSQL client and development files
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the FastAPI app
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.api.endpoints.prediction:router", "--host", "0.0.0.0", "--port", "8000", "--reload"]

