from app.main.models.messier import Messier, MessierImage, MessierVideo, MessierName


def get_all_messiers_catalogues(object):
    messiers = object.query.all()
    return messiers


def get_a_messier_catalogue(object, messier_id):
    messier = object.query.filter_by(id=messier_id).first()
    return messier


def get_messier_by_object_type(object_type: str):
    messiers_by_type = Messier.query.filter_by(
                            Messier.object_type.like(
                                str(object_type)+"%"))
    return messiers_by_type
