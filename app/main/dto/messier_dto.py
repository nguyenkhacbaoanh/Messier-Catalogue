"""
Data Transfert Object
"""

from flask_restplus import Namespace, fields


class MessierDto:
    """
    A class used to represent an Messier's and its used to transfert data

    ...

    Attributes
    ----------
    api : type Namespace of flask restplus
        a defined sub-api
    messier : model data object
        messier model data
    """

    api = Namespace('Messier', description="Messier catalogue")
    messier = api.model(
        # model's name
        'messier',
        # define all fields in this model with their data type
        {
            'messier_id': fields.String(
                  required=True,
                  description='messier reference'),
            'ngc': fields.String(
                   required=True,
                   description='ngc reference'),
            'object_type': fields.String(
                           required=True,
                           description="""nebulae, clusters,
                                          galaxies, and other
                                          kinds of objects not
                                          under any major category
                                       """),
            'season': fields.String(
                      required=True,
                      description='Season'),
            'magnitude': fields.String(
                         required=True,
                         description='magnitude'),
            'constellation_eng': fields.String(
                                 required=True,
                                 description='constellation'),
            'constellation_fr': fields.String(
                                required=True,
                                description='constellation'),
            'constellation_lat': fields.String(
                                 required=True,
                                 description='constellation'),
            'right_ascension': fields.String(
                               required=True,
                               description='right ascension'),
            'declinaison': fields.String(
                           required=True,
                           description='declinaison'),
            'distance': fields.String(
                        required=True,
                        description='distance'),
            'size': fields.String(
                    required=True,
                    description='size'),
            'discoverer': fields.String(
                          required=True,
                          description='discoverer'),
            'year': fields.String(
                    required=True,
                    description='year'),
            'image_URL': fields.String(
                         required=True,
                         description='image_URL'),
            'image_URL1': fields.String(
                          required=True,
                          description='image_URL_download'),
            'constellation': fields.String(
                             required=True,
                             description='constellation')
        })


class MessierDtov2:
    """
    A class used to represent an Messier's and its used to transfert data

    ...

    Attributes
    ----------
    api : type Namespace of flask restplus
        a defined sub-api
    messier : model data object
        messier model data
    """

    api = Namespace('Messier v2', description="Messier catalogue")
    """
    designations = db.Column(ARRAY(db.String))
    # messier = db.Column(db.String(120), unique=True, nullable=False)
    # ngc = db.Column(db.String(100), unique=True, nullable=False)
    type = db.Column(db.String(100))
    object = db.Column(db.String(100))
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
    class = db.Column(db.String(100))
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
    """
    messier = api.model(
        # model's name
        'messier v2',
        # define all fields in this model with their data type
        {
            'id': fields.String(
                  # required=True,
                  description='messier reference'),
            'designations': fields.List(fields.String),
            'type': fields.String(
                           # required=True,
                           description="""nebulae, clusters,
                                          galaxies, and other
                                          kinds of objects not
                                          under any major category
                                       """),
            'object': fields.String(
                      # required=True,
                      description='Season'),
            'features': fields.String(
                         # required=True,
                         description='magnitude'),
            'constellation': fields.String(
                                 # required=True,
                                 description='constellation'),
            'right_ascension': fields.String(
                                # required=True,
                                description='constellation'),
            'declinaison': fields.String(
                                 # required=True,
                                 description='constellation'),
            'distance': fields.String(
                               # required=True,
                               description='right ascension'),
            'apparent_magnitude': fields.String(
                           # required=True,
                           description='declinaison'),
            'absolute_magnitude': fields.String(
                        # required=True,
                        description='distance'),
            'apparent_dimensions': fields.String(
                    # required=True,
                    description='size'),
            'radius': fields.String(
                          # required=True,
                          description='discoverer'),
            'class': fields.String(
                    # required=True,
                    description='year'),
            'age': fields.String(
                         # required=True,
                         description='image_URL'),
            'year': fields.String(
                          # required=True,
                          description='image_URL_download'),
            'number_of_stars': fields.String(
                             # required=True,
                             description='constellation'),
            'tidal_radius': fields.String(
                             # required=True,
                             description='constellation'),
            'mass': fields.String(
                             # required=True,
                             description='constellation'),
            'size': fields.String(
                             # required=True,
                             description='constellation'),
            'redshift': fields.String(
                             # required=True,
                             description='constellation'),
            'helio_radial_velocity': fields.String(
                             # required=True,
                             description='constellation'),
            'galactocentric_velocity': fields.String(
                             # required=True,
                             description='constellation'),
            'linear_diameter': fields.String(
                             # required=True,
                             description='constellation'),
            'spectral_class': fields.String(
                             # required=True,
                             description='constellation'),
            'diameter': fields.String(
                             # required=True,
                             description='constellation'),
            'heliocentric_radial_velocity': fields.String(
                             # required=True,
                             description='constellation'),
            'galactocentric_radial_velocity': fields.String(
                             # required=True,
                             description='constellation'),
            'discoverer': fields.String(
                             # required=True,
                             description='constellation'),
            'image': fields.List(fields.Url),
            'video': fields.List(fields.Url)
                            
        })
