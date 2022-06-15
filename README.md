
# Every week, every new playlist

This week I'm listening to
Tydzień 18 - Mexico[Spotify Link](https://open.spotify.com/playlist/4lBPXYsuC55wcn6cs54bdV)
Scripts in this repositories can let you generate randomly playlist from Spotify's nation-origin genres.

List of genres were taken from [everynoise.com/everynoise1d.cgi?scope=all](https://everynoise.com/everynoise1d.cgi?scope=all).
From those, the nation-origins ones were selected using list of every nations adjectives from [Wikipedia](https://en.wikipedia.org/wiki/List_of_adjectival_and_demonymic_forms_for_countries_and_nations) (probably not the best solution, but English adjectives are not declined).

## Instalation

Create `config.json` like this

```json
{
    "username": "",
    "api_credentials": "",
    "data": ""
}
```

and fill right information.
Then `api_credentials.json` like this

```json
{
    "client_ID": "",
    "client_SECRET": "",
    "redirect_uri": "/"
}
```

and fill with API credentials from your spotify developer account.

## Instalation on Raspberry Pi

Install appropriate packages (spotipy will be sufficient) in venv via pip. Create `job.sh` file like this

```sh
#! /bin/bash
SCRIPT_PATH='path2dirwithmainpy'
cd $SCRIPT_PATH
path2python/python -m main
```

Then one can create cron job like this.

```sh
crontab -e```
add the line for the job. Eg.
```0 0 * * MON /home/pi/src/weekly-playlist-chooser/job.sh```
this will make script run every Monday at midnight.

## TODO

- [ ] Check for existing playlist (in current week) and prompt for confirmation.
- [ ] Check for duplicate (see above, but it's not likely to duplicate two same genres). In following weeks there shouldn't be
 the same playlist drawed as was previously.
- [ ] Web interface, publicly available.
- [ ] Some analysys.
