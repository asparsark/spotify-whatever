from flask import Flask, request, redirect
from config import load, update
import auth_requests as ar, os


_app = Flask(__name__)
_app_quit = False

def auth_init():
    cfg = load()
    _app.config.cfg = cfg

    if not _refresh(cfg):
        _app.run()
        # add browser tab opening magic
        #webbrowser.open('http://localhost:5000', new=2)


def _refresh(cfg):
    if cfg['refresh_token']:
        res = ar.refresh_token(cfg['client_id'], cfg['client_secret'], cfg['refresh_token'])

        if 'access_token' in res:
            update({'access_token': res['access_token']})
            return True
        else: 
            update({'refresh_token': ''})
            return False


@_app.route('/')
def init():
    client_id, redirect_uri = _app.config.cfg['client_id'], _app.config.cfg['redirect_uri']

    callback = ar.auth_url(client_id, redirect_uri)

    return redirect(callback)


@_app.route('/callback')
def callback():
    if 'code' in request.args:
        code = request.args['code']
        client_id, client_secret, redirect_uri = _app.config.cfg['client_id'], _app.config.cfg['client_secret'], _app.config.cfg['redirect_uri']

        res = ar.access_token(code, client_id, client_secret, redirect_uri)

        if 'access_token' in res:
            update({'access_token': res['access_token'], 'refresh_token': res['refresh_token']})

    return redirect('exit')
        

@_app.route('/exit')
def exit_app():
    global _app_quit
    _app_quit = True

    return "Exiting"


@_app.teardown_request
def teardown(e):
    if _app_quit:
        os._exit(0)