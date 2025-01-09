# Use an official Python runtime
FROM python:3.9-slim

# Working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY app/ /app/app

# Expose the Flask port
EXPOSE 5000

# Default command
CMD ["python", "app/main.py"]
