import string


info_preamble = """
# Every week, every new playlist

This week I'm listening to
"""

def save_playlist_info2json(data):
    with open('infos/playlist_history.json', 'r+') as f:
        import json
        try:
            old = json.load(f)
        except json.JSONDecodeError:
            old = {}
        
        import datetime
        key = data['id']
        data['week'] = datetime.date.today().isocalendar()[1]
        old[key] = data
        
        f.seek(0) # treat file as empty
        json.dump(old,f,indent=4, sort_keys=True)


def read_playlist_info(id):
    """from JSON

    Args:
        id (string): ID
    """
    with open('infos/playlist_history.json', 'r') as f:
        import json
        data = json.load(f)
        return data[id]

# def update_info(country, genre, markdown_file='current_week.md'):
def update_info(playlist_id):
    """Adding info to README about what i'm listening this week from JSON

    Args:
        playlist_id (string): ID
    """
    project_info = ''
    with open('infos/project_info.md', 'r') as f:
        project_info = f.read()
    with open('infos/current_playlist.md','w') as f:
        f.write(info_preamble)
        
        playlist_info = read_playlist_info(playlist_id)
        
        current_playlist_line = str(playlist_info['title']) +  r'[Spotify Link](' + str(playlist_info['url']) +')'
        f.write(current_playlist_line + '\n')   
        
        with open('README.md','w') as readme:
            readme.write(info_preamble)
            readme.write(current_playlist_line + '\n')    
            readme.write(project_info)
        