FROM python:3.12-alpine
WORKDIR /app

# Installer les dépendances système minimales
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev

# Installer les dépendances du systèmes et supprimer les dépendances alpine
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && apk del .build-deps

# Copier tous les fichiers
COPY . .

# Rouler les tests
CMD ["pytest"]