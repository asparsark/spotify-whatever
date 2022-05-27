import const
import base64, json, requests
import flask

API_URL = 'https://accounts.spotify.com'

def userAuth():

    return f'''{API_URL}/authorize?response_type=code&client_id={const.CLIENT_ID}&redirect_uri={const.REDIRECT_URI}'''

def requestAccessToken(code):

    body = {
        'grant_type': 'authorization_code',
        'code' : code,
        'redirect_uri': const.REDIRECT_URI,
        'client_id': const.CLIENT_ID,
        'client_secret': const.CLIENT_SECRET
    }

    enc1 = f'{const.CLIENT_ID}:{const.CLIENT_SECRET}'
    enc2 = base64.b64encode(enc1.encode()).decode()
    print(enc2)

    headers = {
        'Content-Type' : 'application/x-www-form-urlencoded', 
        'Authorization' : f'Basic {enc2}'
    }

    post = requests.post(f'{API_URL}/api/token', params=body, headers=headers)

    return post