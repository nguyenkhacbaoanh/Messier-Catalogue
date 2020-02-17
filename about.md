# Project fil rouge:
  Projet data web et api
  CATALOGUE DE GALAXIES

## Des membres du groupe:
    1. NGUYEN Khac Bao Anh
    2. CABON Antoine
    3. SOLOZABAR Marie

## Les données que contiendront votre catalogue (Messier):

1. Messier v1: Notre V1 ne se concentre que sur le premier catalogue de Messier. On a 
  - id (messier)
  - L'image 
  - Le nom objets
  - Saison
  - Magnitude 
  - dimension
  - distance
  - Right ascension 
  - declinaison
  - constellation (english)
  - constellation (fr)
  - découvreur 
  - Année

2. Messier v2 (Messier amélioré): apres du webscraping nous avons pu enrichir le notre V1 pour avoir plus d'information, tout en recherchant les doublons. 
  - id (messier)
  - designations
  - messier_type
  - messier_object
  - features
  - constellation
  - right_ascension
  - declinaison
  - distance
  - apparent_magnitude
  - absolute_magnitude
  - apparent_dimensions
  - radius
  - messier_class
  - age
  - year
  - number_of_stars
  - tidal_radius
  - mass
  - size
  - redshift
  - helio_radial_velocity
  - galactocentric_velocity
  - linear_diameter
  - spectral_class
  - diameter
  - heliocentric_radial_velocity
  - galactocentric_radial_velocity
  - discoverer
  - image
  - video

## L'intérêt scientifique de ces données et de votre catalogue:

connaitre mieux les objets et créer un catalogue de renseignement pour le débutant ou l'experimenté.  

## Les fonctionnalités minimales de votre outil de consultation:

Une bar de recherche. Nous aimerions partir sur des simples mot cléf permet de retrouver des galaxies.
Les méthodes d'API RESTful:
  1. /api/v2/messier-catalogue                         GET

  ```curl -X GET "http://anh.pythonanywhere.com/api/v2/messier-catalogue/" -H "accept: application/json"```

  2. /api/v2/messier-catalogue/<messier_id>           GET

  ```curl -X GET "http://anh.pythonanywhere.com/api/v2/messier-catalogue/M1" -H "accept: application/json"```

  3. /api/v2/messier-catalogue/<messier_id>    DELETE
  4. /api/v2/messier-catalogue/    PUT/PATCH
  5. /api/v2/messier-catalogue/                POST

## Les fonctionnalités idéales de votre outil

Pour la bar de recherche, nous souhaitons utiliser l'expression regulière (Regex).

## Les resources de donnée:

1. [Messier v1 - en premier-matière](https://www.datastro.eu/explore/dataset/catalogue-de-messier/table/?disjunctive.objet&disjunctive.mag&disjunctive.english_name_nom_en_anglais&disjunctive.french_name_nom_francais&disjunctive.latin_name_nom_latin&sort=messier)
  - Nous souhaitons recuperer les données: [lien](https://www.datastro.eu/explore/dataset/catalogue-de-messier/table/?disjunctive.objet&disjunctive.mag&disjunctive.english_name_nom_en_anglais&disjunctive.french_name_nom_francais&disjunctive.latin_name_nom_latin&sort=messier). On peut sauvegarder les données dans une base de donnée sqlite en différents environnements (DEV-TEST-PROD).
  - La data téléchargée sur le site de datastro, ils sont les features pertinentes mais qu'il y a beaucoup de feature doublée, il y a pas bien de travailler sur cette data

2. [Messier v2 - version évoluée](https://www.messier-objects.com/messier-object-list/)
  - Le but est d'enrichir la data, nous avons utiliser le web scraping pour parser des éléments (informations) dans des articles et aussi les liens des images et des videos

## Les technologies pressenties pour réaliser le projet:

1. API - Server - CORS - Authorization - Sécurité:
  - Flask
  - Flask-restful
  - Flask-Cors
  - Okta: c'est le cloud software qui nous permets de builder les access management.

  Notre api a utilisé Swagger UI pour l'interface d'utilisateur et a implémenté des authorizations et authentifications utilisées deux choix: **Token** ou **Oauth2 implicit**

2. Object-relational Mapping, gestions des versions de donnée et importation
  - Flask-SQLAlchemy
  - Pandas
  - Flask-Migrate

3. Ajouter des commandes supplémentaires et les extensions du scripts Flask
  - Flask-Script

4. Test unitaire et test styles, normes du code:
  - unittest
  - flake8

5. Web Scraping
  - selenium
  - jupyter notebook
  - beautifulsoup

Notre dernier objectif est de faire le lien entre le site et l'api. 
