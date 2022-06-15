import random
import re

def get_random_notEmpty_country_genres(c_dict):
    """Drawing genres and countries from previously generated/loaded c_dict - dictionary of spotifies genres

    Args:
        c_dict (dict): spotify country: genres

    Returns:
        string: string of country and genre
    """
    while True:
        country, genres = random.choice(list(c_dict.items()))
        if len(genres) > 0:
            break
    return country, genres

def make_query_search(genre):
    """Spotify search query

    Args:
        genre (string): 

    Returns:
        string: 
    """
    genre_ = re.sub(' ', '_', genre)
    return rf'genre:{genre_}'

import spotipy
from spotipy.oauth2 import SpotifyOAuth

def playlist_title_descr(country, genre):
    """Preparing title string with current week (in year scale) number

    Args:
        country (string): 
        genre (string): 

    Returns:
        string: 
    """
    import datetime
    n_of_week = datetime.date.today().isocalendar()[1]
    
    playlist_title = f'Tydzień {n_of_week} - {country}' #TODO Tydzień [0-9] roku 2022 itp
    playlist_title = playlist_title.title()
    
    playlist_descr = f'Tydzień {n_of_week}. Muzyka z gatunku: {genre.title()} z {country.title()}'
    
    return playlist_title, playlist_descr

def save_spotify_playlist(c_dict, username, credentials):
    """interface to spotify allowing to create and push randomly choosen playlist to Spotify

    Args:
        c_dict (dict): country: genres
        username (string): spotify username
        credentials (dict): dict eg. loaded from json. dict_keys(['client_ID', 'client_SECRET', 'redirect_uri'])
    Returns:

    """
    scope = "playlist-modify-public"
    # sp_playlist = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_ID,
    #     client_secret= cred.client_SECRET, redirect_uri=cred.redirect_uri, scope=scope, open_browser=False))
    sp_playlist = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=credentials['client_ID'],
        client_secret= credentials['client_SECRET'], redirect_uri=credentials['redirect_uri'], scope=scope, open_browser=False))
    
    random_country, random_genre = get_random_notEmpty_country_genres(c_dict)
    random_genre = random.choice(random_genre) # Losowanie Kategorii
    search = sp_playlist.search(make_query_search(random_genre),market='PL',type='track', limit=50)
    uris = [item['uri'] for item in search['tracks']['items']]

    playlist_title, playlist_descr = playlist_title_descr(random_country, random_genre)
    playlist = sp_playlist.user_playlist_create(user=username, name=playlist_title, public=True,description=playlist_descr)
    playlist_id = playlist['id']
    playlist_url = playlist['external_urls']['spotify']

    sp_playlist.user_playlist_add_tracks(username, playlist_id, tracks=uris, position=None)
    
    history_data = {'title': playlist_title, 'descr': playlist_descr, 'id': playlist_id, 'url': playlist_url}
    
    from update_info import save_playlist_info2json
    save_playlist_info2json(history_data)
    
    return playlist_id