import web_scraping
import randoming_spotify
import credentials
import update_info

# adding current directory to PATH in order to be able to run main.py as script
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

c_dict = web_scraping.read_c_dict('c_dict.json')
credent = credentials.read_credentials('api_credentials.json')
username = credentials.read_config('config.json')['username']
playlist_id = randoming_spotify.save_spotify_playlist(c_dict, username='papah4',credentials=credent)
update_info.update_info(playlist_id)