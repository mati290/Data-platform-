FROM python:3.11-slim

# 1️⃣ System dependencies (KRYTYCZNE)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 2️⃣ Workdir
WORKDIR /app

# 3️⃣ Python deps
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 4️⃣ App code
COPY . .

EXPOSE 8000

# 5️⃣ Run API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
