#!/usr/bin/env python3

from flask import request
from flask_restful import Resource

from src.ext.auth import validate_query

from ..querys.cpf  import Query


class CpfResource(Resource):
  def post(self):
    token  = request.headers.get("Authorization", None)
    verify = validate_query(token=token)

    if not verify["isvalid"]:
      return verify["response"]

    cpf = request.form.get("cpf", None)
    return Query(data=cpf).response()
