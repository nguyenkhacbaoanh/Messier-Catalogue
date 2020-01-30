"""
Data Transfert Object
"""

from flask_restplus import Namespace, fields

class MessierDto:
    api = Namespace('Messier', description="Messier catalogue")
    messier = api.model('messier', {
                                    'id': fields.String(required=True, description='messier reference'),
                                    'ngc': fields.String(required=True, description='messier reference'),
                                    'object_type': fields.String(required=True, description='messier reference'),
                                    'season': fields.String(required=True, description='messier reference'),
                                    'magnitude': fields.String(required=True, description='messier reference'),
                                    'constellation_eng': fields.String(required=True, description='messier reference'),
                                    'constellation_fr': fields.String(required=True, description='messier reference'),
                                    'constellation_lat': fields.String(required=True, description='messier reference'),
                                    'right_ascension': fields.String(required=True, description='messier reference'),
                                    'declinaison': fields.String(required=True, description='messier reference'),
                                    'distance': fields.String(required=True, description='messier reference'),
                                    'size': fields.String(required=True, description='messier reference'),
                                    'discoverer': fields.String(required=True, description='messier reference'),
                                    'year': fields.String(required=True, description='messier reference'),
                                    'image_URL': fields.String(required=True, description='messier reference'),
                                    'constellation': fields.String(required=True, description='messier reference')
                                })