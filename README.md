**Antoine CABON, NGUYEN Khac Bao Anh, SOLOZABAR Marie**

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
