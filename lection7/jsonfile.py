import json

def func(dict):
    with open('jsonFile.json', 'w') as jf:
        json.dump(dict, jf)
