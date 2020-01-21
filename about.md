# Project fil rouge:
  Projet data web et api
  CATALOGUE DE GALAXIES

## Des membres du groupe:
    1. NGUYEN Khac Bao Anh
    2. CABON Antoine
    3. SOLOZABAR Marie

## Les données que contiendront votre catalogue (Messier amélioré):

ref messier
L'image 
Le nom objets
Saison
Magnitude 
dimension
distance
Right ascension 
declinaison
constellation (english)
constellation (fr)
découvreur 
Année

## L'intérêt scientifique de ces données et de votre catalogue:

connaitre mieux les objets et créer un catalogue de renseignement pour le débutant ou l'experimenté.  

## Les fonctionnalités minimales de votre outil de consultation:

Une bar de recherche. Nous aimerions partir sur des simples mot cléf permet de retrouver des galaxies. 

## Les fonctionnalités idéales de votre outil:

Pour la bar de recherche, nous souhaitons utiliser l'expression regulière (Regex). 

## Les technologies pressenties pour réaliser le projet:

Flask
Celery 
Postgre
Redis

On utilise flask pour le serveur l'API rest. 

Nous souhaitons recuperer les données: https://www.datastro.eu/explore/dataset/catalogue-de-messier/table/?disjunctive.objet&disjunctive.mag&disjunctive.english_name_nom_en_anglais&disjunctive.french_name_nom_francais&disjunctive.latin_name_nom_latin&sort=messier. On peut sauvegarder les données dans une base de donnée Postgres. 

Celery sera utilisé pour gerer les performances. Celery permet de créer des taches de fond donc plusieurs utilisateurs peuvent faire des requetes sur l'API en même temps. 

Redis intervient avant celery et envoie les requetes dans des systèmes de distributions qui permet de gerer les utilisateurs et leurs requetes un par un. 

