from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

import pandas as pd

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/catalogue-database.db'
db = SQLAlchemy(app)

class Catalogue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    messier = db.Column(db.String(120), unique=True, nullable=False)
    ngc = db.Column(db.String(100), unique=True, nullable=False)
    object_type = db.Column(db.String(100), unique=True, nullable=False)
    season= db.Column(db.String(100), unique=True, nullable=False)
    magnitude = db.Column(db.String(100), unique=True, nullable=False)
    constellation_eng = db.Column(db.String(100), unique=True, nullable=False)
    constellation_fr = db.Column(db.String(100), unique=True, nullable=False)
    constellation_lat = db.Column(db.String(100), unique=True, nullable=False)
    right_ascension = db.Column(db.String(100), unique=True, nullable=False)
    declinaison = db.Column(db.String(100), unique=True, nullable=False)
    distance = db.Column(db.String(100), unique=True, nullable=False)
    size = db.Column(db.String(100), unique=True, nullable=False)
    discoverer = db.Column(db.String(100), unique=True, nullable=False)
    year = db.Column(db.String(100), unique=True, nullable=False)
    image_URL = db.Column(db.String(500), unique=True, nullable=False)
    constellation = db.Column(db.String(100), unique=True, nullable=False)

df = pd.read_csv('catalogue-de-messier.csv', sep=';')
df.to_sql(name="catalogue", con=db.engine, if_exists='replace', index=False)

@app.route('/api/messier-catalogue', methods=['GET'])
def messier_catalogue():

    all_catalogues = Catalogue.query.all()

    data ={'data': []}

    for x in all_catalogues:
        cat = {}
        cat['id'] = x.id
        cat['messier'] = x.messier
        cat['ngc'] = x.ngc
        cat['object_type'] = x.object_type
        cat['season'] = x.season
        cat['magnitude'] = x.magnitude
        cat['constellation_eng'] = x.constellation_eng
        cat['constellation_fr'] = x.constellation_fr
        data['data'].append(cat)

    return data

if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=5000)