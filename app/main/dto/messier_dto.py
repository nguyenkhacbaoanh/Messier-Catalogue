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
            'id': fields.String(
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

    api = Namespace('Messier v2', description="Messier catalogue advance")

    messier_name = api.model(
        'messier name list',
        {
            "other_name": fields.String(attribute="designations")
        }
    )

    messier_image = api.model(
        'messier image',
        {
            "image_url": fields.String(attribute="image"),
            "image_description": fields.String(500, attribute="image_desc")
        }
    )

    messier_video = api.model(
        'messier video',
        {
            "video_url": fields.String(attribute="video"),
        }
    )

    messier = api.model(
        # model's name
        'messier v2',
        # define all fields in this model with their data type
        {
            'id': fields.String(
                  # required=True,
                  description='messier reference'),
            'designations': fields.List(fields.Nested(messier_name)),
            'messier_type': fields.String(
                           # required=True,
                           description="""nebulae, clusters,
                                          galaxies, and other
                                          kinds of objects not
                                          under any major category
                                       """),
            'messier_object': fields.String(
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
            'declination': fields.String(
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
            'messier_class': fields.String(
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
            'image': fields.List(fields.Nested(messier_image)),
            'video': fields.List(fields.Nested(messier_video))
        })

    messier_playload = api.model(
        # model's name
        'messier form',
        # define all fields in this model with their data type
        {
            'id': fields.String(
                  # required=True,
                  description='messier reference'),
            'messier_type': fields.String(
                           # required=True,
                           description="""nebulae, clusters,
                                          galaxies, and other
                                          kinds of objects not
                                          under any major category
                                       """),
            'messier_object': fields.String(
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
            'declination': fields.String(
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
            'messier_class': fields.String(
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
                             description='constellation')
        })
