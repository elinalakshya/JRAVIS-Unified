# Mission2040 Intelligence Worker - Clean Dockerfile
FROM python:3.10-slim

# Set working directory for build and runtime
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy worker code
COPY . .

# Force runtime directory
WORKDIR /app

# Start the intelligence worker
CMD ["python", "mission2040_intelligence_worker.py"]
