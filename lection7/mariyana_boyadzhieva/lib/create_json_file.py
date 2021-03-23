import json


def dict_to_json(dict_info):
    with open("paragraph_info_json.json", "w") as outfile:
        json.dump(dict_info, outfile, indent=4)
