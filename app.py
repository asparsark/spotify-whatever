from flask import Flask, request, redirect
import const
import auth
import webbrowser

app = Flask(__name__)

#webbrowser.open('http://localhost:5000', new=2)

@app.route("/")

def user():
    url = auth.userAuth()

    return redirect(url)

@app.route("/yas")

def callback():
    code = request.args['code']

    res = auth.requestAccessToken(code)

    return res.text