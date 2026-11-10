from fastapi import FastAPI, status
from datetime import datetime

# 1. Create the FastAPI app instance
app = FastAPI(
    title="CCTNS Intelligence Layer API",
    description="Backend service for police decision support",
    version="1.0.0"
)

# 2. Root Endpoint (HTTP GET /)
@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {
        "message": "CCTNS Intelligence Layer API is running",
        "status": "online",
        "documentation": "/docs"
    }

# 3. Health Check Endpoint (HTTP GET /health)
# In GCP, Google checks this URL to see if your container is healthy
@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "cctns-core-api"
    }