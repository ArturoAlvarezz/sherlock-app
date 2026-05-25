# Use python 3.11-slim for a smaller footprint, compatible with ARM64
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Clone Sherlock
RUN git clone https://github.com/sherlock-project/sherlock.git .

# Install Sherlock via pyproject.toml (Poetry-based)
RUN pip install --no-cache-dir .

# Install our custom backend dependencies
COPY requirements.txt /tmp/backend-requirements.txt
RUN pip install --no-cache-dir -r /tmp/backend-requirements.txt

# Copy our custom backend logic
COPY ./app /app/app
COPY ./data /app/data

# Ensure the app package is discoverable
ENV PYTHONPATH=/app

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
