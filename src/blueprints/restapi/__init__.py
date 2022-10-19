from flask import Blueprint
from flask_restful import Api

from .resource.cpf  import CpfResource
from .resource.nome import NomeResource

bp = Blueprint("restapi", __name__, url_prefix="/v1")
api = Api(bp)


def init_app(app):
  api.add_resource(CpfResource, "/cpf/")
  api.add_resource(NomeResource, "/nome/")
  app.register_blueprint(bp)
