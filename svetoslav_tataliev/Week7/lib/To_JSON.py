import json


def create_json(dic: dict):
    with open("JSON_Output.json", "w") as outfile:
        json.dump(dic, outfile)
