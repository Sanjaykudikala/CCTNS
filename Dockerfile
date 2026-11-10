# 1. Base Image: lightweight official Python 3.11 Linux runtime
FROM python:3.11-slim

# 2. Create and switch to a clean /app directory inside the container
WORKDIR /app

# 3. Copy requirements and install packages inside the container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy your main.py code into the container's /app folder
COPY . .

# 5. Inform Docker that our application listens on port 8000
EXPOSE 8000

# 6. The command to start the server when the container boots up
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]