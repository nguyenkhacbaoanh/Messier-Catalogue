import os

from app.main import db
from app.main.models.messier import Messier
from manage import BASEDIR
from app.main.utils import ingestion_init_data

from app.test.base import BaseTestCase


class TestMessier(BaseTestCase):

    def test_importing_data(self):
        ingestion_init_data(
            os.path.join(
                BASEDIR,
                "data/catalogue-de-messier2.csv"),
            ",",
            db.engine,
            "messier")
        _messier = Messier.query.filter_by(id='M22').first()
        self.assertTrue(
            isinstance(_messier, Messier),
            "get a messier object in db and test it's type")
        self.assertTrue(
            _messier.id == 'M22',
            "id requested is in database")

    def test_get_all_messier_objects(self):
        ingestion_init_data(
            os.path.join(
                BASEDIR,
                "data/catalogue-de-messier2.csv"),
            ",",
            db.engine,
            "messier")
        _messiers = Messier.query.all()
        self.assertTrue(
            isinstance(_messiers, list),
            "get all messier object and it's a list type")
        self.assertFalse(
            len(_messiers) < 110,
            "messier database contain at least 110 categories")
