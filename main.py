from flask import Flask, request, make_response, redirect, render_template, session

app = Flask('_name_')

app.config['SECRET_KEY'] = 'Osva-0807_App $'

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", error=error)

@app.route('/')
def index ():
    user_ip = request.remote_addr
    response = make_response(redirect("/home"))
    session['user_ip'] = user_ip
    return response

@app.route('/home')
def home():
    user_ip = session.get('user_ip')
    response = render_template("home.html", user_ip=user_ip)
    return response