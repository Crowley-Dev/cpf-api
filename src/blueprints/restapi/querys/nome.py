#!/usr/bin/env python3

from flask import jsonify, request
from sqlalchemy import func

from unicodedata import normalize

from src.model import Pessoas


class Query:
  def __init__(self, data):
    self.data = str(data)

  def response(self):
    validate = self.data.replace(" ", "").isalpha()
    if not validate:
      return jsonify(
        status=404,
        data="Isso não é um nome."
      )

    query = self.nome(self.data)
    if query is not None:
      return query

    return jsonify(
      status=204,
      data="Não encontrado na nossa base de dados."
    )


  def nome(self, nome):
    nome = normalize('NFKD', nome).encode('ASCII', 'ignore')
    nome = nome.decode('ASCII')

    pessoas = Pessoas.query.filter(
      func.lower(Pessoas.nome) == func.lower(nome)
    )

    if pessoas.first() is not None:
      return jsonify(
        status = 200,
        data = [
          pessoa.to_dict()
          for pessoa in pessoas
        ],
      )
