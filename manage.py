import os
# import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db
# from app.main.models import catalogue
from app.main.utils import ingestion_init_data

BASEDIR = os.path.dirname(os.path.abspath(__name__))

app = create_app(os.getenv("APP_ENV") or "dev")
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command("db", MigrateCommand)


@manager.command
def run():
    app.run()


@manager.command
def import_data():
    ingestion_init_data("catalogue-de-messier.csv", ";", db.engine, "messier")


if __name__ == '__main__':
    manager.run()
