import json

def print_json(dict_json):
    out_file = open("output.json", "w")
    json.dump(dict_json, out_file, indent=6)
    out_file.close()