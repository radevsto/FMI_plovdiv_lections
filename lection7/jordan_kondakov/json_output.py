import string
import json


def to_json(dict_structure):
    json_file = open("json_formated_file.txt", "w+")
    json_file.write(json.dumps(dict_structure))
    json_file.close()
