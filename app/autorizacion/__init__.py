from flask import Blueprint

auth = Blueprint("autorizacion", __name__, url_prefix="/autorizacion")

from . import views
