import web_scraping
import randoming_spotify
import credentials

c_dict = web_scraping.read_c_dict('c_dict.json')
credent = credentials.read_credentials('api_credentials.json')
username = credentials.read_config('config.json')['username']
country, genre = randoming_spotify.save_spotify_playlist(c_dict, username='papah4',credentials=credent)
