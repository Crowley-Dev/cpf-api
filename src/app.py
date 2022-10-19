#!/usr/bin/env python3

from flask import Flask
from src.ext import configuration


def minimal_app(**config):
  app = Flask(__name__)
  configuration.init_app(app, **config)
  return app


def create_app(**config):
  app = minimal_app(**config)
  configuration.load_extensions(app)
  return app


server = create_app()
# server.run(port=5000)
