from .. import db
from marshmallow import Schema

class Messier(db.Model):
    __tablename__ = "messier"

    id = db.Column(db.Integer, primary_key=True)
    # messier = db.Column(db.String(120), unique=True, nullable=False)
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
    year = db.Column(db.Integer(), unique=True, nullable=False)
    image_URL = db.Column(db.String(500), unique=True, nullable=False)
    image_URL1 = db.Column(db.String(500), unique=True, nullable=False)
    constellation = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return "<Messier '{}'>".format(self.id)

# class MessierSchema(Schema):
#     class Meta:
#         # Fields to expose
#         fields = ("id", "messier", "ngc", "object_type", "season", "magnitude", "constellation_eng", "constellation_fr", "constellation_lat", "right_ascension", "declinaison", "distance", "size", "discoverer", "year", "image_URL", "constellation")

#     # Smart hyperlinking
#     _links = ma.Hyperlinks(
#         {"self": ma.URLFor("detail", id="<id>")}
#     )