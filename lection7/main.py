import argparse
import re
import jsonfile
import csvfile

parser = argparse.ArgumentParser(description="Name of textfile")
parser.add_argument("--text", type=str, help='The name of the textfile')
args = parser.parse_args()

f = open(args.text, "r")
x = re.findall(r"## Begin (.*)\n(.*)\n## End", f.read())

dict = {}

for item in x:
    key = item[0]

    if key not in dict:
        dict[key] = {}

    splitted = item[1].split()
    dict[key]["name"] = splitted[0]
    dict[key]["type"] = splitted[1].split('=')[1]
    dict[key]["format"] = splitted[2].split('=')[1]

jsonfile.func(dict)
csvfile.func(dict)

f.close()

