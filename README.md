**Antoine CABON, NGUYEN Khac Bao Anh, SOLOZABAR Marie**

Application est déployé sur pythonanywhere.com : [site](http://anh.pythonanywhere.com/)

Application:  Voici la structure de l'application, le schéma permet de voir comment est pensé la structure de notre projet.

    messier-catalogue/
                    ├── Makefile
                    ├── README.md
                    ├── __init__.py
                    ├── about.md
                    ├── app
                    │   ├── __init__.py
                    │   ├── main
                    │   │   ├── __init__.py
                    │   │   ├── catalogue-database-dev.db
                    │   │   ├── catalogue-database-test.db
                    │   │   ├── config.py
                    │   │   ├── dto
                    │   │   │   ├── __init__.py
                    │   │   │   └── messier_dto.py
                    │   │   ├── models
                    │   │   │   ├── __init__.py
                    │   │   │   └── messier.py
                    │   │   ├── routes
                    │   │   │   ├── __init__.py
                    │   │   │   ├── messier_routes.py
                    │   │   │   └── messier_v2_routes.py
                    │   │   ├── services
                    │   │   │   ├── __init__.py
                    │   │   │   └── messier_services.py
                    │   │   └── utils.py
                    │   └── test
                    │       ├── __init__.py
                    │       ├── base.py
                    │       ├── test_config.py
                    │       └── test_messier.py
                    ├── data
                    │   ├── catalogue-de-messier2.csv
                    │   ├── designations.csv
                    │   ├── images.csv
                    │   ├── images2.csv
                    │   ├── messier-catalogue-evolue2.csv
                    │   └── videos2.csv
                    ├── gunicorn.py
                    ├── manage.py
                    ├── requirements.txt
                    ├── run_app.sh
                    └── wsgi.py

Download all dependencies: télécharger les dépendances

    pip install -r requirements.txt

Initialize database: initaliser la database 
    
    # Initialize database with table defined
    python manage.py db init 
    python manage.py db migrate
    python manage.py db upgrade
    # Two command below to ingest csv data to sqlite database
    python manage.py import_data
    python manage.py db migrate --message "initialize data from csv file"


Start app: ```make all``` démarrer l'application

    # clean app
    make clean
    # install packages dependencies
    make python-packages
    # initialize database
    make database
    # run tests
    make tests
    # run app
    make run


App launch on [127.0.0.1:5000](127.0.0.1:5000)

