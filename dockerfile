# Dockerfile for FastAPI with ML Model

# Use the official Python image as a base
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

#copy requirements file first to leverage Docker cache
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the FastAPI app will run on
EXPOSE 8085

# Command to run the FastAPI application using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8085"]