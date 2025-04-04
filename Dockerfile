# Base image officielle Python
FROM python:3.12-slim

# Répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code
COPY . .

# Port à exposer
EXPOSE 8080

# Lancer l'app Flask
CMD ["python", "app.py"]