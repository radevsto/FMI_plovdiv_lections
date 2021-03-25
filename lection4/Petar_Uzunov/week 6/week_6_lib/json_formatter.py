import json

def format(data):
    with open('dump.json', 'w') as file:
        json.dump(data, file, indent=4)
    file.close()
