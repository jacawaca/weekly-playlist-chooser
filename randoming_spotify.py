import random
import re

def get_random_notEmpty_country_genres(c_dict):
    while True:
        country, genres = random.choice(list(c_dict.items()))
        if len(genres) > 0:
            break
    return country, genres

def make_query_search(genre):
    genre_ = re.sub(' ', '_', genre)
    return rf'genre:{genre_}'

import spotipy
from spotipy.oauth2 import SpotifyOAuth

def playlist_title_descr(country, genre):
    import datetime
    n_of_week = datetime.date.today().isocalendar()[1]
    
    playlist_title = f'Tydzień {n_of_week} - {country}'
    playlist_title = playlist_title.title()
    
    playlist_descr = f'Tydzień {n_of_week}. Muzyka z gatunku: {genre.title()} z {country.title()}'
    
    return playlist_title, playlist_descr

def save_spotify_playlist(c_dict, username, credentials):
    scope = "playlist-modify-public"
    # sp_playlist = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_ID,
    #     client_secret= cred.client_SECRET, redirect_uri=cred.redirect_uri, scope=scope, open_browser=False))
    sp_playlist = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=credentials['client_ID'],
        client_secret= credentials['client_SECRET'], redirect_uri=credentials['redirect_URI'], scope=scope, open_browser=False))
    
    random_country, random_genre = get_random_notEmpty_country_genres(c_dict)
    random_genre = random.choice(random_genre) # Losowanie Kategorii
    search = sp_playlist.search(make_query_search(random_genre),market='PL',type='track')
    uris = [item['uri'] for item in search['tracks']['items']]

    user = 'papah4'
    playlist_title, playlist_descr = playlist_title_descr(random_country, random_genre)
    playlist = sp_playlist.user_playlist_create(user=user, name=playlist_title, public=True,description=playlist_descr)
    playlist_id = playlist['id']

    sp_playlist.user_playlist_add_tracks(user, playlist_id, tracks=uris, position=None)