from app.main import db
from app.main.models.messier import Messier

def get_all_messiers_catalogues():
    # messiers_schema = MessierSchema(many=True)
    messiers = Messier.query.all()
    # results = {"data": messiers_schema.dump(messiers)}
    return messiers

def get_a_messier_catalogue(messier_id):
    # messier_schema = MessierSchema()
    messier = Messier.query.filter_by(id=messier_id).first()
    # result = {"data": messier_schema.dump(messier)}
    return messier