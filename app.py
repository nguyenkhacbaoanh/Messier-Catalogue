from flask import Flask
from flask import request

from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

import os

import pandas as pd

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}/catalogue-database.db'.format(os.path.dirname(os.path.abspath(__file__)))
db = SQLAlchemy(app)

from catalogue import Catalogue

# flask marshmallow
# requirements.txt 

@app.route('/api/messier-catalogue', methods=['GET'])
def messier_catalogue():

    all_catalogues = Catalogue.query.all()
    print(all_catalogues)

    data ={'data': []}

    for catalogue in all_catalogues:
        cat = {}
        cat['id'] = catalogue.id
        cat['messier'] = catalogue.messier
        cat['ngc'] = catalogue.ngc
        cat['object_type'] = catalogue.object_type
        cat['season'] = catalogue.season
        cat['magnitude'] = catalogue.magnitude
        cat['constellation_eng'] = catalogue.constellation_eng
        cat['constellation_fr'] = catalogue.constellation_fr
        cat['constellation_lat'] = catalogue.constellation_lat
        cat['right_ascension']= catalogue.right_ascension
        cat['declinaison'] = catalogue.declinaison
        cat['distance'] = catalogue.distance
        cat['size'] = catalogue.size
        cat['discoverer'] = catalogue.discoverer
        cat['year'] = catalogue.year
        cat['image_URL'] = catalogue.image_URL
        cat['constellation'] = catalogue.constellation

        data['data'].append(cat)

    return data

@app.route('/api/messier-catalogue/<ref>', methods=['GET'])
def get_messier_catalogue(ref):

    catalogue = Catalogue.query.filter_by(id=ref).first()
    data = {'data': []}

    cat = {}
    cat['id'] = catalogue.id
    cat['messier'] = catalogue.messier
    cat['ngc'] = catalogue.ngc
    cat['object_type'] = catalogue.object_type
    cat['season'] = catalogue.season
    cat['magnitude'] = catalogue.magnitude
    cat['constellation_eng'] = catalogue.constellation_eng
    cat['constellation_fr'] = catalogue.constellation_fr
    cat['constellation_lat'] = catalogue.constellation_lat
    cat['right_ascension']= catalogue.right_ascension
    cat['declinaison'] = catalogue.declinaison
    cat['distance'] = catalogue.distance
    cat['size'] = catalogue.size
    cat['discoverer'] = catalogue.discoverer
    cat['year'] = catalogue.year
    cat['image_URL'] = catalogue.image_URL
    cat['constellation'] = catalogue.constellation
    data['data'].append(cat)
    
    return data

@app.route('/api/messier-catalogue/<ref>/delete', methods=['DELETE'])
def delete_messier_catalogue(ref):

    catalogue = Catalogue.query.filter_by(id=ref).first()
    db.session.delete(catalogue)
    db.session.commit()

    return {'data' : ' {} has been deleted.'.format(ref)}

# {
# "id":"M1",
# "messier":"test", 
# "ngc" :"test", 
# "object_type" :"test", 
# "season": "test",
# "magnitude":"test", 
# "constellation_eng":"test", 
# "constellation_fr": "test", 
# "constellation_lat":"test",
# "right_ascension":"test", 
# "declinaison": "test",
# "distance": "test",
# "size": "test",
# "discoverer" : "test", 
# "year": "test", 
#  "image_URL": "test", 
# "constellation": "test"}
@app.route('/api/messier-catalogue/update', methods=['GET', 'POST'])
def update_messier_catalogue():

    catalogue = Catalogue.query.filter_by(id=request.json['id']).first()

    catalogue.messier = request.json['messier']
    catalogue.ngc = request.json['ngc'] 
    catalogue.object_type = request.json['object_type']
    catalogue.season = request.json['season']
    catalogue.magnitude = request.json['magnitude']
    catalogue.constellation_eng = request.json['constellation_eng']
    catalogue.constellation_fr = request.json['constellation_fr']
    catalogue.constellation_lat= request.json['constellation_lat']
    catalogue.right_ascension = request.json['right_ascension']
    catalogue.declinaison = request.json['declinaison']
    catalogue.distance = request.json['distance']
    catalogue.size = request.json['size']
    catalogue.discoverer = request.json['discoverer']
    catalogue.year = request.json['year']
    catalogue.image_URL = request.json['image_URL']
    catalogue.constellation = request.json['constellation']

    db.session.commit()

    return {'data' : ' {} has been updated.'.format(request.json['id'])}

@app.route('/api/messier-catalogue/create', methods=['GET', 'POST'])
def create_messier_catalogue():

    new_catalogue = Catalogue(
                        id=request.json['id'], 
                        messier= request.json['messier'], 
                        ngc = request.json['ngc'], 
                        object_type = request.json['object_type'], 
                        season= request.json['season'], 
                        magnitude= request.json['magnitude'], 
                        constellation_eng =request.json['constellation_eng'],
                        constellation_fr = request.json['constellation_fr'],
                        constellation_lat = request.json['constellation_lat'],
                        right_ascension = request.json['right_ascension'],
                        declinaison = request.json['declinaison'],
                        distance = request.json['distance'],
                        size =request.json['size'],
                        discoverer = request.json['discoverer'], 
                        year = request.json['year'], 
                        image_URL = request.json['image_URL'], 
                        constellation = request.json['constellation'])
    
    db.session.add(new_catalogue)
    db.session.commit()

    return {'data' : ' {} has been created.'.format(request.json['id'])}

if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=5000)