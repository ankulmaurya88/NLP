# Use lightweight Python image
FROM python:3.11-slim

WORKDIR /app

# Copy backend code
COPY backend/ /app/backend

# Copy requirements
COPY backend/requirement.txt /app/requirement.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Expose backend port
EXPOSE 8000

# Run FastAPI app with Gunicorn + Uvicorn
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "backend.app:app", "--bind", "0.0.0.0:8000"]
