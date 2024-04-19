
# Tcom MVP 

Application de visualisation et gestion de travaux. Accès aux documents nécessaires, géolocalisation des sites, upload de photos. 
Gestion des accès utilisateurs : nécessité de posséder un compte pour se connecter. Un compte "démo" peut être créé. 
Le front est adapté aux mobiles. 

Disclaimer : Adaptation d'un projet réel. Toutes les informations sensibls ont été retirées ou anonymisées. Il peut en résulter des erreurs. Ne pas utiliser tel quel, et envoyez un feedback en cas de problème. 


**Infos techniques** 
L'application est développée dans des containers Docker : 
    - la BDD -> container "db_tcom" 
    - l'application -> container "app_tcom" 
    - Adminer (gestion de la BDD) -> container "adminer_tcom" 
Framework : Django 
BDD : PostgreSQL 


## Structure du dossier 

+  API (Django Rest Framework) 
    + commands : fichiers permettant de lancer des commandes à partir du terminal 
    + project : partie config et commune du projet 
        - asgi.py 
        - settings.py 
        - urls.py 
        - wsgi.py 
    + templates 
        - base.html 
    + uthdemo : fonctionnalités métier 
        + images/ 
        + models/ 
        + serializers/ 
        + static/ 
        + templates/ 
        + utils/ 
        - admin.py 
        - apps.py 
        - forms.py 
        - permissions.py  
        - signals.py 
        - urls.py 
        - views.py 
    - dockerfile 
    - manage.py 
    - requirements.txt 
- compose.yaml 


## Commandes utiles 

Pour lancer une commande : 
1. Ouvrir le fichier qui porte le nom de la commande 
2. Vérifier les données (noms de fichiers par exemple) 
3. Modifier si besoin 
4. Se placer à la racine de l'API dans le terminal et taper : `./<command>` du nom du fichier. 


