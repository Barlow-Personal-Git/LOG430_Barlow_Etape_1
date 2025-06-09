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
Créer une base de donnée PostgreSQL et configurez les paramètres de connexion dans app/db.py
```
psql -U postgres
CREATE DATABASE log430_lab;
```

1. Seed de la base de données
```
python3 seed/run_seed.py 
```

1. Exécuter le programme
```
python3 app.py
```
