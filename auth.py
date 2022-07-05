import os
from flask import Flask, request, redirect

import config
import auth_requests as ar

_app = Flask(__name__)
_app_quit = False

def auth_init():
    config_data = config.load()

    if not _refresh(config_data):
        _app.config.config_data = config_data
        _app.run()
        # add browser tab opening magic
        #webbrowser.open('http://localhost:5000', new=2)

def _refresh(config_data):
    if config_data.refresh_token:
        res = ar.refresh_token(config_data.client_id, config_data.client_secret, config_data.refresh_token)

        if 'access_token' in res:
            config.update({'access_token': res['access_token']})

            return True
        else: 
            config.update({'refresh_token': ''})

    return False

@_app.route('/')
def init():
    config_data = _app.config.config_data

    callback = ar.auth_url(config_data.client_id, config_data.redirect_uri)

    return redirect(callback)

@_app.route('/callback')
def callback():
    if 'code' in request.args:
        code = request.args['code']
        config_data = _app.config.config_data

        res = ar.access_token(code, config_data.client_id, config_data.client_secret, config_data.redirect_uri)

        if 'access_token' in res:
            config.update({'access_token': res['access_token'], 'refresh_token': res['refresh_token']})

    return redirect('exit')
        
@_app.route('/exit')
def exit_app():
    global _app_quit
    _app_quit = True

    return 'Exiting'

@_app.teardown_request
def teardown(e):
    if _app_quit:
        os._exit(0)

if __name__ == '__main__':
    auth_init()
