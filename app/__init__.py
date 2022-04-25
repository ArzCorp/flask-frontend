from flask import Flask
from .config import Config

def create_app():
  app = Flask('_name_')
  app.config.from_object(Config)
  return app