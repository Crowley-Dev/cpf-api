#!/usr/bin/env python3

from flask import jsonify, request

from validate_docbr import CPF

from src.model import Pessoas

import re


class Query:
  def __init__(self, data):
    numbers = re.compile("[^0-9]")
    self.data = numbers.sub("", str(data))

  def response(self):
    validate = lambda data: CPF().validate(data)
    if not validate(self.data):
      return jsonify(
        status=404,
        data="CPF inexistente."
      )

    query = self.cpf(self.data)
    if query is not None:
      return query

    return jsonify(
      status=204,
      data="Não encontrado na nossa base de dados."
    )


  def cpf(self, cpf):
    response = Pessoas.query.filter_by(cpf=cpf).first()
    if response is not None:
      return jsonify(
        status=200,
        data=response.to_dict(),
      )
