from flask import Flask
from flask import request

from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

import os

import pandas as pd

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}/catalogue-database.db'.format(os.path.dirname(os.path.abspath(__file__)))
db = SQLAlchemy(app)
ma = Marshmallow(app)

from catalogue import Catalogue

from catalogue_schema import CatalogueSchema, catalogues_schema, catalogue_schema

@app.route('/api/messier-catalogue', methods=['GET'])
def messier_catalogue():
    catalogues = Catalogue.query.all()
    return {'data' : catalogues_schema.dump(catalogues)}

@app.route('/api/messier-catalogue/<ref>', methods=['GET'])
def get_messier_catalogue(ref):

    catalogue = Catalogue.query.filter_by(id=ref).first()
    return {'data' : catalogue_schema.dump(catalogue)}

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