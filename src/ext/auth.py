#!/usr/bin/env python3

from datetime import date
from src.model import Clientes

from flask import (
  jsonify, request, make_response
)


def verify_user(token: str):
  user  = Clientes.query.filter_by(token=token).first()

  if not user:
    return {
      "isvalid": False,
      "response": make_response(
        jsonify(
          status=403,
          data="Token inexistente."
        ), 403
      )
    }

  time = [int(num) for num in user.created_at.split("-")]
  expired = date.today() - date(*time)
  if expired.days > int(user.plano):
    return {
      "isvalid": False,
      "response": make_response(
        jsonify(
          status=401,
          data="Token expirou."
        ), 401
      )
    }

  return {
    "isvalid": True,
    "response": user
  }


def validate_query(token: str):
  verify = verify_user(token=token)
  if not verify["isvalid"]:
    return verify

  user = verify["response"]
  data = request.form.keys()

  if not [x for x in data if x in ("cpf", "nome")]:
    return {
      "isvalid": False,
      "response": make_response(
        jsonify(
          status=400,
          data="Informação a ser consultada não foi definida."
        ), 400
      )
    }

  return {
    "isvalid": True
  }


