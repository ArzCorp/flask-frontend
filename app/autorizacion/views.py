from flask import render_template
from . import auth
from app.forms import LoginForm

@auth.route("/ingresar")
def login():
  form = LoginForm()
  context = {
    'form': form
  }
  return render_template("login.html", **context)