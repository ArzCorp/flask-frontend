from flask import request, make_response, redirect, render_template, session, flash

from app import create_app
from app.forms import LoginForm

app = create_app()

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", error=error)

@app.route('/')
def index ():
    user_ip = request.remote_addr
    response = make_response(redirect("/inicio"))
    session['user_ip'] = user_ip
    return response

@app.route('/inicio')
def home():
    user_ip = session.get('user_ip')
    response = render_template("home.html", user_ip=user_ip)
    return response

@app.route('/ingresar', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if request.method == "GET":
        response = render_template("login.html", form=form)
        return response
    else:
        if form.validate_on_submit():
            return make_response(redirect("/inicio"))
        else:
            flash("Verifica tus datos")
            response = render_template("login.html", form=form)
            return response