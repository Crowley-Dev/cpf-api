from src.ext.database import db
from sqlalchemy_serializer import SerializerMixin

from .entities.pessoas import Pessoas


class Clientes(db.Model, SerializerMixin):
  __bind_key__ = "users"

  token        = db.Column(
    db.Text,
    primary_key=True,
  )

  nome         = db.Column(db.Text)
  email        = db.Column(db.Text)
  plano        = db.Column(db.Text)
  created_at   = db.Column(db.Text)


class Owner(db.Model, SerializerMixin):
  __bind_key__ = "users"

  token = db.Column(
    db.Text,
    primary_key=True,
  )

  nome  = db.Column(db.Text)
  email = db.Column(db.Text)
