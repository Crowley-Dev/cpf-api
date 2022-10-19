#!/usr/bin/env python3

from flask import render_template, request, abort
from dynaconf import settings


def home():
  host = request.headers.get("Host", None)
  if host not in settings.HOSTS:
    return abort(403)
  return render_template("index.html"), 200
