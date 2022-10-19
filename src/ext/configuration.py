#!/usr/bin/env python3

from importlib import import_module
from dynaconf import FlaskDynaconf


def load_extensions(app):
  for extension in app.config.EXTENSIONS:
    module_name, factory = extension.split(":")
    ext = import_module(module_name)
    getattr(ext, factory)(app)


def init_app(app, **config):
  FlaskDynaconf(app, **config)
