# ue19-lab-05
Random Joke Generator
===================================

Description
-----------
Cette application interroge l'API "Official Joke API" pour afficher une blague.

Fichiers
--------
- app.py : le programme principal
- requirements.txt : les dépendances Python
- Dockerfile : le fichier pour créer et exécuter le conteneur Docker
- README.md : ce fichier d'explication

Installation
------------
1. Cloner le dépôt :
   git clone https://github.com/<ton-utilisateur>/ue19-lab-05.git
   cd ue19-lab-05

2. Installer les dépendances :
   pip install -r requirements.txt

Utilisation
-----------
Pour exécuter l'application :
   python app.py

Exécution avec Docker
---------------------
1. Construire l'image Docker :
   docker build -t ue19-lab-05 .

2. Lancer le conteneur :
   docker run --rm ue19-lab-05
