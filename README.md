**Antoine CABON, NGUYEN Khac Bao Anh, SOLOZABAR Marie**

Application Structure

    messier-catalogue/
                    ├── README.md
                    ├── about.md
                    ├── app
                    │ ├── init.py
                    │ ├── catalogue-de-messier.csv
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

Download all dependencies: 

    pip install -r requirements.txt

Initialize database:
    
    # Initialize database with table defined
    python manage.py db init 
    python manage.py db migrate
    python manage.py db upgrade
    # Two command below to ingest csv data to sqlite database
    python manage.py import_data
    python manage.py db migrate --message "initialize data from csv file"


Start app: 

    python manage.py run
    # application will run on port 5000
