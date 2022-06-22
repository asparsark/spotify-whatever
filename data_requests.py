import requests, json

API_URI = 'https://api.spotify.com/v1'

def generate_headers(access_token):
    headers = {
        'Authorization' : f'Bearer {access_token}',
        'Content-Type' : 'application/json'
    }

    return headers

def get_profile(access_token):
    headers = generate_headers(access_token)

    res = requests.get(f'{API_URI}/me', headers=headers)

    return json.loads(res.text)

def get_user_playlists(access_token, offset=0):
    headers = generate_headers(access_token)

    res = requests.get(f'{API_URI}/me/playlists?limit=50&offset={offset}', headers=headers)

    return json.loads(res.text)
