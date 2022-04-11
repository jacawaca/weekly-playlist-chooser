# Every week, every new playlist

Scripts in this repositories can let you generate randomly playlist from Spotify's nation-origin genres.

List of genres were taken from [everynoise.com/everynoise1d.cgi?scope=all](https://everynoise.com/everynoise1d.cgi?scope=all).
From those, the nation-origins ones were selected using list of every nations adjectives from [Wikipedia](https://en.wikipedia.org/wiki/List_of_adjectival_and_demonymic_forms_for_countries_and_nations) (probably not the best solution, but English adjectives are not declined).

## Instalation

Create `config.json` like this

```json
{
    "username": ""
}
```

and fill with your spotify username.
Then `api_credentials.json` like this

```json
{
    "client_ID": "",
    "client_SECRET": "",
    "redirect_uri": "/"
}
```

and fill with API credentials from your spotify developer account.

## TODO

- [ ] Check for existing playlist (in current week) and prompt for confirmation.
- [ ] Check for duplicate (see above, but it's not likely to duplicate two same genres). In following weeks there shouldn't be
 the same playlist drawed as was previously.
- [ ] Some analysys.
