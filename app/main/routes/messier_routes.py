from flask import request
from flask_restplus import Resource

from app.main.dto.messier_dto import MessierDto
from app.main.services.messier_services import *

api = MessierDto.api
_messier = MessierDto.messier


@api.route("/")
class ListMessierCatalogue(Resource):
    @api.doc('list_of_messier_catalogue')
    @api.marshal_list_with(_messier, envelope='data')
    def get(self):
        return get_all_messiers_catalogues()