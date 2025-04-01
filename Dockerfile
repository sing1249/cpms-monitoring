# Use slim Python image for smaller size
FROM python:3.11-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY app.py .
COPY app_insights_fetch.py .
COPY azure_monitor_fetch.py .

# Expose Flask port
EXPOSE 5000

# Run the Flask app using Gunicorn for production
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
