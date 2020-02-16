**Antoine CABON, NGUYEN Khac Bao Anh, SOLOZABAR Marie**

Application:  Voici la structure de l'application, le schéma permet de voir comment est penser la structure de notre projet.

    messier-catalogue/
                    ├── README.md
                    ├── about.md
                    ├── app
                    │ ├── init.py
                    │ ├── main
                    │ │ ├── init.py
                    │ │ ├── catalogue-database-dev.db
                    │ │ ├── config.py
                    │ │ ├── dto
                    │ │ │ ├── init.py
                    │ │ │ └── messier_dto.py
                    │ │ ├── models
                    │ │ │ ├── init.py
                    │ │ │ └── messier.py
                    │ │ ├── routes
                    │ │ │ ├── init.py
                    │ │ │ └── messier_routes.py
                    │ │ ├── services
                    │ │ │ ├── init.py
                    │ │ │ └── messier_services.py
                    │ │ └── utils.py
                    │ ├── test
                    │ └── wsgi.py
                    ├── catalogue-de-messier.csv
                    ├── deployement
                    │ ├── ansibles
                    │ │ ├── inventory
                    │ │ └── playbook
                    │ │ └── main.yml
                    │ ├── aws_keys.yml
                    │ └── server-api-messier.pem
                    ├── manage.py
                    └── requirements.txt

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

