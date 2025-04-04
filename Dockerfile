FROM python:3.12-slim

# Install dependencies
RUN apt-get update && apt-get install -y gcc git libssl-dev

# Set workdir
WORKDIR /app

# Copy project files
COPY . /app

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# Port (Railway détecte automatiquement)
ENV PORT=8080

# Launch app
CMD ["python", "app.py"]
