from flask_testing import TestCase

from app.main import db
from manage import app

class BaseTestCase(TestCase):
    """
    Base Tests for application

    ...
    Methods
    --------
    create_app
        configurate testing case
    
    setUp
        create all table name
    
    shutDown
        remove database and clean environment
    """

    def create_app(self):
        """ set database for testing case """
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def setUp(self):
        """ start testing with database up """
        db.create_all()
        db.session.commit()

    def tearDown(self):
        """ remove & clean database """
        db.session.remove()
        db.drop_all()