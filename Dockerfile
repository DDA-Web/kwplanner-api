# Rebuild triggered le 4 avril 2025

FROM python:3.11-slim

WORKDIR /app

# Ajout des outils système requis par grpc
RUN apt-get update && apt-get install -y gcc build-essential libssl-dev && apt-get clean

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
