# Utilise une image Python légère avec les outils nécessaires
FROM python:3.11-slim

# Installe les dépendances système nécessaires à grpcio
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    python3-dev \
    libssl-dev \
    libffi-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copie les fichiers
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose le port
EXPOSE 8080

# Lance l'app Flask
CMD ["python", "app.py"]
