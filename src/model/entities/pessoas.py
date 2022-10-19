from src.ext.database import db
from sqlalchemy_serializer import SerializerMixin


class Pessoas(db.Model, SerializerMixin):
  cpf    = db.Column(
    db.Text,
    primary_key=True
  )

  nome   = db.Column(db.Text)
  estado = db.Column(db.Text)
  cidade = db.Column(db.Text)
