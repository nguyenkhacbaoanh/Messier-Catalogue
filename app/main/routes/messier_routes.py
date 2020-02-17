from flask_restplus import Resource, abort

from app.main.models.messier import Messier

from app.main.dto.messier_dto import MessierDto
from app.main.services.messier_services import (
    get_all_messiers_catalogues,
    get_a_messier_catalogue
)

api = MessierDto.api
_messier = MessierDto.messier


@api.route("/")
class ListMessierCatalogue(Resource):
    @api.doc('list_of_messier_catalogue')
    @api.marshal_list_with(_messier, envelope='data')
    def get(self):
        return get_all_messiers_catalogues(Messier)


@api.route("/<messier_id>")
class MessierCatalogue(Resource):
    @api.doc('messier_catalogue_detail')
    # @api.doc(security='apikey')
    @api.marshal_with(_messier, envelope='data')
    @api.response(200, "Success")
    @api.response(401, "Not authorize")
    @api.response(400, "Bad requests")
    # @token_required
    def get(self, messier_id):
        result = get_a_messier_catalogue(Messier, messier_id)
        if result is None:
            abort(400)
        else:
            return get_a_messier_catalogue(Messier, messier_id)
