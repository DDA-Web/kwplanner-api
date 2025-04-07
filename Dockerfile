# Utilise une image Python officielle
FROM python:3.12-slim

# Empêche les buffers sur les logs
ENV PYTHONUNBUFFERED=1

# Crée un répertoire de travail
WORKDIR /app

# Copie les fichiers nécessaires
COPY requirements.txt .

# Installe les dépendances système minimales
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Installe les dépendances Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copie le reste des fichiers
COPY . .

# Définit le port d'écoute
EXPOSE 8080

# Démarre l'application Flask
CMD ["python", "app.py"]
