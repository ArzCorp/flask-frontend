from flask import Flask, request, make_response, redirect

app = Flask('_name_')

@app.route('/')
def hello ():
  user_ip = request.remote_addr
  response = make_response(redirect("/home"))
  response.set_cookie("user_ip", user_ip)
  return response

@app.route('/home')
def Home():
    user_ip = request.cookies.get("user_ip")
    return "Home" + " " + user_ip