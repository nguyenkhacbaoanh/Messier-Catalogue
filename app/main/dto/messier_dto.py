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
