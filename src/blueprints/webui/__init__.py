#!/usr/bin/env python3

from flask import Blueprint, render_template
# from .views import home


bp = Blueprint(
  "webui",
  __name__,
  template_folder="templates",
  static_folder="static",
  static_url_path="/src/blueprints/webui/static"
);

# bp.add_url_rule("/", view_func=home)


def init_app(app):
  app.register_blueprint(bp)


@bp.app_errorhandler(405)
def error405(error):
  return render_template(
    "error.html",
    title_error="Método não permitido.",
    code_error=405,
    content_error="O método não é permitido para a URL solicitada."
  ), 405


@bp.app_errorhandler(404)
def error404(error):
  return render_template(
    "error.html",
    title_error="Página não encontrada.",
    code_error=404,
    content_error="A URL solicitada não foi encontrada neste servidor."
  ), 404


@bp.app_errorhandler(403)
def error403(error):
  return render_template(
    "error.html",
    title_error="Acesso negado.",
    code_error=403,
    content_error="Você não tem permissão para acessar o servidor."
  ), 403


@bp.app_errorhandler(400)
def error400(error):
  return render_template(
    "error.html",
    title_error="Erro 400. (Bad request)",
    code_error=400,
    content_error="Você fez uma requisição errada."
  ), 400


@bp.app_errorhandler(500)
def error500(error):
  return render_template(
    "error.html",
    title_error="Erro no servidor interno.",
    code_error=500,
    content_error="Ocorreu um erro interno no servidor."
  ), 500
