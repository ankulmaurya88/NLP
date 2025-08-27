FROM python:3.11-slim

WORKDIR /app

# Copy ML model and related scripts
COPY ml_model/ /app/ml_model

# Copy backend requirements (for packages like scikit-learn, pandas, etc.)
COPY backend/requirement.txt /app/requirement.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Expose ML service port
EXPOSE 9000

# Run FastAPI app for ML predictions
CMD ["gunicorn", "-w", "2", "-k", "uvicorn.workers.UvicornWorker", "ml_model.predict:app", "--bind", "0.0.0.0:9000"]
