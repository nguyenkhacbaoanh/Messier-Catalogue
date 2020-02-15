.PHONY: clean system-packages python-packages install tests database run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	find . -type f -name '*.log' -delete
	find . -type f -name '*.db' -delete
	find . -type d -name 'migrations' -delete

system-packages:
	sudo apt install python-pip -y

python-packages:
	pip install -r requirements.txt

install: system-packages python-packages

tests:
	python manage.py test
	flake8 --exclude migrations,env,__pycache__,.git

database:
	python manage.py db init
	python manage.py db migrate
	python manage.py db upgrade
	python manage.py import_data
	python manage.py db migrate --message "initialize data from csv file"

run:
	python manage.py run

all: clean python-packages database tests run