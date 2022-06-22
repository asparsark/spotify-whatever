#import csv

import config
import data_requests as dr
from auth import auth_init

#5l3M71C51ZHmr17liwvujW
playlist_csv = '/data/user_playlists.csv'

# find him a new home
def test_token(access_token):
    res = dr.get_profile(access_token)

    if 'error' not in res:
        return True

def playlists(playlist_filepath=playlist_csv):
    cfg = config.load()

    if not test_token(cfg['access_token']):
        auth_init()

    return getter(cfg['access_token'])

# e handler + logger
def getter(access_token, counter=0):

    batch = dr.get_user_playlists(access_token, counter)
    counter+=50

    for i in batch['items']:
        # Commas in playlist names!! (different append altogether)
        # name,tracks.total,id,external_urls.spotify
        item_str = f'{i["name"]},{i["tracks"]["total"]},{i["id"]},{i["external_urls"]["spotify"]}'

        with open('playlists_test.csv', 'a') as f:
            f.write(f'{item_str},\n')

    if counter > batch['total']:
        print('Done')
        return True
    else:
        return getter(access_token, counter)
