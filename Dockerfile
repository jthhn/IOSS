# Use official Python image
FROM python:3.12-slim

WORKDIR /app

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the app code
COPY . .

# Expose the port
EXPOSE 5000

# Command to run Flask app
CMD ["python", "run.py"]
