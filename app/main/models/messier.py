from .. import db


class Messier(db.Model):
    """
    A class used to represent a Messier object

    ...

    Attributes
    ----------
    __tablename__ : str
        a formatted string to represent data table name
    id : str
        messier's id
    ngc : str
        messier corresponds to ngc's name
    object_type : str
        groups type object

    Methods
    -------
    __repr__
        represent a object's messier - printed by it's id
    """

    __tablename__ = "messier"

    id = db.Column(db.Integer, primary_key=True)
    # messier = db.Column(db.String(120), unique=True, nullable=False)
    ngc = db.Column(db.String(100), unique=True, nullable=False)
    object_type = db.Column(db.String(100), unique=True, nullable=False)
    season = db.Column(db.String(100), unique=True, nullable=False)
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
