from flask import Flask, request, redirect
import config
import auth
import webbrowser

app = Flask(__name__)

#webbrowser.open('http://localhost:5000', new=2)


@app.route('/')

def initAuth():
    callback = auth.userAuth(config.CLIENT_ID, config.REDIRECT_URI)

    return redirect(callback)


@app.route('/callback')

def callback():
    code = request.args['code']

    res = auth.requestAccessToken(code, config.REDIRECT_URI, config.CLIENT_ID, config.CLIENT_SECRET)

    # make that shit persist txt or smth
    config.REFRESH_TOKEN = res['access_token']

    return res


@app.route('/refresh_token')

def getRefreshToken():
    return 'yeet'