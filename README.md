# LOG430_Lab1

## Prérequis
Avant de commencer, assurez-vous d'avoir les éléments suivants :
- Python 3.x
- PostgreSQL

## Installation
1. Cloner le repo
```
git clone https://github.com/Barlow-Personal-Git/LOG430_Barlow_Etape_1.git
```
2. Créer et activer un environnement virtuel:
```
python3 -m venv env
source env/bin/activate
```

Note : Si vous avez besoin de déactive
```
deactive
```

3. Installer les dépendances:
```
pip install -r requirements.txt
```

4. Configurer PostgreSQL
Créer une base de donnée PostgreSQL
```
psql -U postgres
CREATE DATABASE log430_lab;
```

5. Configurer les variables d'environnement
Copier le fichier d'exemple et renommez-le :
```
cp .env-example .env
```
Ensuite, ouvrez le fichier `.env` et modifiez la variable `DATABASE_URL` :
- Remplacez `user` par le nom de votre utilisateur
- Remplacez `password` par le mot de passe de cet utilisateur
- Remplez `table` par le nom de votre base de données (ex.: log430_lab)

6. Seed de la base de données
```
python3 seed/run_seed.py 
```

## Exécution
1. Exécuter le programme
```
python3 app.py
```


