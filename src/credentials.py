import json

def read_credentials(json_file='api_credentials.json'):
    with open(json_file, 'r') as f:
        credent = json.load(f)
    return credent

def read_config(json_file='config.json'):
    with open(json_file, 'r') as f:
        configs = json.load(f)
    return configs
