import base64, json, requests

API_URL = 'https://accounts.spotify.com'

def userAuth(client_id, redirect_uri):

    return f'''{API_URL}/authorize?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}'''


def generateHeaders(client_id, client_secret):

    enc1 = f'{client_id}:{client_secret}'
    enc2 = base64.b64encode(enc1.encode()).decode()

    headers = {
        'Content-Type' : 'application/x-www-form-urlencoded', 
        'Authorization' : f'Basic {enc2}'
    }

    return headers


def requestAccessToken(code, redirect_uri, client_id, client_secret):

    body = {
        'grant_type': 'authorization_code',
        'code' : code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret
    }

    headers = generateHeaders(client_id, client_secret)

    res = requests.post(f'{API_URL}/api/token', params=body, headers=headers)

    return json.loads(res.text)


def requestRefreshToken(refresh_token, client_id, client_secret):

    body = {
        'grant_type': 'refresh_token',
        'refresh_token' : refresh_token,
    }

    headers = generateHeaders(client_id, client_secret)

    res = requests.post(f'{API_URL}/api/token', params=body, headers=headers)

    return json.loads(res.text)