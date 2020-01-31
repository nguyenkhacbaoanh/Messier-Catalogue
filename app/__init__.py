from flask_restplus import Api
from flask import Blueprint

from app.main.routes.messier_routes import api as messier_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Messier Catalogue',
          version='1',
          description="School's project"
          )

api.add_namespace(messier_ns, path='/api/v1/messier-catalogue')
