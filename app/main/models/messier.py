from .. import db
from sqlalchemy.types import ARRAY


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

class MessierV2(db.Model):
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

    __tablename__ = "messierv2"

    id = db.Column(db.Integer, primary_key=True)
    designations = db.Column(ARRAY(db.String))
    # messier = db.Column(db.String(120), unique=True, nullable=False)
    # ngc = db.Column(db.String(100), unique=True, nullable=False)
    type_ = db.Column(db.String(100))
    object_ = db.Column(db.String(100))
    features = db.Column(db.String(100))
    constellation = db.Column(db.String(100))
    #constellation_eng = db.Column(db.String(100))
    #constellation_fr = db.Column(db.String(100))
    #constellation_lat = db.Column(db.String(100))
    right_ascension = db.Column(db.String(100))
    declinaison = db.Column(db.String(100))
    distance = db.Column(db.String(100))
    apparent_magnitude = db.Column(db.String(100))
    absolute_magnitude = db.Column(db.String(100))
    apparent_dimensions = db.Column(db.String(100))
    radius = db.Column(db.String(100))
    class_ = db.Column(db.String(100))
    age = db.Column(db.String(100))
    year = db.Column(db.Integer())
    number_of_stars = db.Column(db.String(100))
    tidal_radius = db.Column(db.String(100))
    mass = db.Column(db.String(100))
    size = db.Column(db.String(100))
    redshift = db.Column(db.String(100))
    helio_radial_velocity = db.Column(db.String(100))
    galactocentric_velocity = db.Column(db.String(100))
    linear_diameter = db.Column(db.String(100))
    spectral_class = db.Column(db.String(100))
    diameter = db.Column(db.String(100))
    heliocentric_radial_velocity = db.Column(db.String(100))
    galactocentric_radial_velocity = db.Column(db.String(100))
    discoverer = db.Column(db.String(100))
    image = db.Column(ARRAY(db.String))
    video = db.Column(ARRAY(db.String))

    def __repr__(self):
        return "<Messier '{}'>".format(self.id)
