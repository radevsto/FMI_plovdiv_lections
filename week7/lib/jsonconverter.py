import json


def convert_to_json(output_data, paragraph, name, file_type, file_format):
    output_data[paragraph] = []
    output_data[paragraph].append({
        'name': name,
        'type': file_type,
        'format': file_format
    })


def write_to_json(data):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, indent=3)
