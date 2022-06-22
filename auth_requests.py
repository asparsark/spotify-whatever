import base64, requests, json

API_URL_AUTH = 'https://accounts.spotify.com'

def auth_url(client_id, redirect_uri):
    scope = 'playlist-read-private'
    return f'{API_URL_AUTH}/authorize?response_type=code&scope={scope}&client_id={client_id}&redirect_uri={redirect_uri}'

def generate_headers(client_id, client_secret):
    enc1 = f'{client_id}:{client_secret}'
    enc2 = base64.b64encode(enc1.encode()).decode()

    headers = {
        'Content-Type' : 'application/x-www-form-urlencoded', 
        'Authorization' : f'Basic {enc2}'
    }

    return headers

def access_token(code, client_id, client_secret, redirect_uri):
    body = {
        'grant_type': 'authorization_code',
        'code' : code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret
    }

    headers = generate_headers(client_id, client_secret)

    res = requests.post(f'{API_URL_AUTH}/api/token', params=body, headers=headers)

    return json.loads(res.text)

def refresh_token(client_id, client_secret, refresh_token):
    body = {
        'grant_type': 'refresh_token',
        'refresh_token' : refresh_token,
    }

    headers = generate_headers(client_id, client_secret)

    res = requests.post(f'{API_URL_AUTH}/api/token', params=body, headers=headers)

    return json.loads(res.text)
