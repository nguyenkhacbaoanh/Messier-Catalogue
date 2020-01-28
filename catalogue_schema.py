from app import ma

class CatalogueSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "ngc", "object_type", "season", "magnitude", "constellation_eng", "constellation_fr", "constellation_lat", "right_ascension", "declinaison", "distance", "size", "discoverer", "year", "image_URL", "image_URL1" ,"constellation")

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {"self": ma.URLFor("detail", id="<id>")}
    )

catalogue_schema = CatalogueSchema()
catalogues_schema = CatalogueSchema(many=True)