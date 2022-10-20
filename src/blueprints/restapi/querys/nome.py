#!/usr/bin/env python3

from flask import (
  jsonify, request, make_response
)

from sqlalchemy import func

from unicodedata import normalize

from src.model import Pessoas


class Query:
  def __init__(self, data):
    self.data = str(data)

  def response(self):
    validate = self.data.replace(" ", "").isalpha()
    if not validate:
      return make_response(
        jsonify(
          status=400,
          data="Isso não é um nome."
        ), 400
      )

    query = self.nome(self.data)
    if query is not None:
      return query

    return make_response(
      jsonify(
        status=404,
        data="Não encontrado na nossa base de dados."
      ), 404
    )


  def nome(self, nome):
    nome = normalize('NFKD', nome).encode('ASCII', 'ignore')
    nome = nome.decode('ASCII')

    pessoas = Pessoas.query.filter(
      func.lower(Pessoas.nome) == func.lower(nome)
    )

    if pessoas.first() is not None:
      return make_response(
        jsonify(
          status = 200,
          data = [
            pessoa.to_dict()
            for pessoa in pessoas
          ],
        ), 200
      )
