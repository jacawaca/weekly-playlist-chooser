import web_scraping
import randoming_spotify
import credentials
import update_info

c_dict = web_scraping.read_c_dict(credentials.read_config('config.json')['data'])
credent = credentials.read_credentials(credentials.read_config('config.json')['api_credentials'])
username = credentials.read_config('config.json')['username']
playlist_id = randoming_spotify.save_spotify_playlist(c_dict, username='papah4',credentials=credent)
update_info.update_info(playlist_id)