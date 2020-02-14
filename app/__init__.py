from flask_restplus import Api
from flask import Blueprint

from app.main.routes.messier_routes import api as messier_ns
from app.main.routes.messier_v2_routes import api as messier_ns_v2

blueprint = Blueprint('api', __name__)

# define authorization for api method
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    },
    'OAuth2': {
        'type': 'oauth2',
        'flow': 'implicit',
        'authorizationUrl': 'https://dev-515581.okta.com',
        'clientId': '0oa2b1rx76qWv8awq357',
        'scopes': {
            'openid': 'Get ID token',
            'profile': 'Get identify',
            'email': 'access by email'
        }
    }
}

api = Api(blueprint,
          title='Messier Catalogue',
          version='1',
          description="School's project",
          authorizations=authorizations
          )

api.add_namespace(messier_ns, path='/api/v1/messier-catalogue')
api.add_namespace(messier_ns_v2, path='/api/v2/messier-catalogue')
