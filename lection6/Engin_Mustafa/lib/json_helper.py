import json


def write_to_file(value: dict):
    with open('json_output.json', 'w') as fp:
        json.dump(value, fp)
