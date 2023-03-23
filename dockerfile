# Utiliser une image Python 3.x
FROM python:3.x

# Installer les dépendances Python
RUN apt-get update && apt-get install -y \
    libpq-dev \
    postgresql-client

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application dans le conteneur
COPY . /app

# Installer les dépendances Python
RUN pip install -r requirements.txt

# Exposer le port 8000 pour le serveur web
EXPOSE 8000

# Lancer le serveur web Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
