from flask import Flask
from .config import Config
from .autorizacion import auth

def create_app():
  app = Flask('_name_')
  app.config.from_object(Config)
  app.register_blueprint(auth)
  return app