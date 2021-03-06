from app.main import db
from flask_restplus import abort


def get_all_messiers_catalogues(object):
    """fetch all object in data table"""
    messiers = object.query.all()
    return messiers


def get_a_messier_catalogue(object, messier_id):
    """fetch object in data table by id"""
    messier = object.query.filter_by(id=messier_id).first()
    return messier


def create_a_messier_catalogue(object, data):
    """
    insert new data to data table

    Parameters:
    object (model): data model
    data (dict): data object
    """
    messier = object.query.filter_by(id=data['id']).first()
    if not messier:
        try:
            new_messier = object(**data)
            save_changes(new_messier)
            return {"message": "Create a new messier successfully"}, 201
        except Exception as e:
            print(e)
            abort(400, "Cannot create a new messier")
    else:
        return {"message": f"Messier {data['id']} existed"}, 200


def update_a_messier_in_catalogue(object, data):
    """
    update data to database

    Parameters:
    object (model): data model
    data (dict): data object
    """
    messier = object.query.filter_by(id=data['id']).first()
    if messier:
        try:
            result = object.query.filter(object.id == data['id']).update(data)
            db.session.commit()
            if result:
                return {"message": f"Update successfully"}, 202
            else:
                return {"message": f"Update failed"}, 400
        except Exception as e:
            print(e)
            abort(400, "Cannot update messier")
    else:
        return {"message": f"Messier {data['id']} not existed"}, 400


def delete_a_messier_in_catalogue(object, messier_id):
    """
    delete a row in data table by id

    Parameters:
    object (model): data model
    messier_id (dict): messier id
    """
    messier = object.query.filter_by(id=messier_id).first()
    if messier:
        try:
            result = object.query.filter(object.id == messier_id).delete()
            db.session.commit()
            if result:
                return {"message": f"Delete successfully"}, 200
            else:
                return {"message": f"Delete failed"}, 400
        except Exception as e:
            print(e)
            abort(400, "Cannot delete messier")
    else:
        return {"message": f"Messier {messier_id} not existed"}, 400


def save_changes(data):
    """validation data and commit it to database"""
    db.session.add(data)
    db.session.commit()
