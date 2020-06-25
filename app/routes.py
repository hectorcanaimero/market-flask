from app.resources.shop import *


def initialize_routes(api):
    api.add_resource(Lojas, '/shop')
    api.add_resource(Loja, '/shop/<string:id>')