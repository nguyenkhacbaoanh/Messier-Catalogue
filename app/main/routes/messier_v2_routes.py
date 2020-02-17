from flask_restplus import Resource, marshal
from app.main.utils import token_required

from app.main.dto.messier_dto import MessierDtov2
from app.main.services.messier_services import (
    get_all_messiers_catalogues,
    get_a_messier_catalogue,
    create_a_messier_catalogue,
    update_a_messier_in_catalogue,
    delete_a_messier_in_catalogue
)
from app.main.models.messier import (
    MessierV2
)

api = MessierDtov2.api
_messier = MessierDtov2.messier
messier_playload = MessierDtov2.messier_playload


@api.route("/<messier_id>")
class MessierCatalogue(Resource):
    @api.doc('messier_catalogue_detail')
    # @api.doc(security='apikey')
    # @api.marshal_with(_messier, skip_none=True, envelope='data', code=200)
    @api.response(200, "Success")
    @api.response(401, "Not authorize")
    @api.response(400, "Bad requests")
    # @token_required
    def get(self, messier_id):
        messier_id = messier_id.upper()
        result = get_a_messier_catalogue(MessierV2, messier_id)
        if result is None:
            return {"message": f"{messier_id} \
                is not existed in our Messier Catalogue"}, 400
        else:
            return marshal(get_a_messier_catalogue(MessierV2, messier_id),
                           _messier, envelope='data', skip_none=True), 200

    @api.doc(security='apikey')
    @token_required
    @api.response(200, "Success")
    @api.response(401, "Not authorize")
    @api.response(400, "Bad requests")
    def delete(self, messier_id):
        messier_id = messier_id.upper()
        return delete_a_messier_in_catalogue(MessierV2, messier_id)


@api.route("/")
class MessierCatalogues(Resource):
    @api.doc('list_of_messier_catalogue')
    # @api.marshal_list_with(_messier, skip_none=True, envelope='data')
    def get(self):
        return marshal(get_all_messiers_catalogues(MessierV2),
                       _messier, skip_none=True, envelope='data'), 200

    # @api.marshal_with(_messier, code=201, skip_none=True)
    @api.expect(messier_playload)
    @api.response(200, "Messier existed")
    @api.response(401, "Not authorize")
    @api.response(400, "Bad requests")
    @api.response(201, "Create successfully")
    @token_required
    @api.doc(security='apikey')
    def post(self):
        return create_a_messier_catalogue(MessierV2, data=api.payload)

    @token_required
    @api.doc(security='apikey')
    @api.expect(messier_playload)
    @api.response(401, "Not authorize")
    @api.response(400, "Bad requests")
    @api.response(202, "Update successfully")
    def put(self):
        return update_a_messier_in_catalogue(MessierV2, data=api.payload)
