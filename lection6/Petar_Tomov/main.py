import re
import argparse
from lib import csv_convert
from lib import json_convert


# Направете програма, която от файл подаден като аргумент прави следното:
# 1. Отваря и прочита файла
def read_and_open_file(path):
    try:
        file = open(path, "r")
        return file.readlines()
    except:
        print("Could not locate file")


# 2. Процесва файла на параграфи. Всеки параграф започва с ## Begin и завършва с ## End
# 3. За всеки параграф направете dictionary структура която има следната структура
# { “paragraph A”: { “name”: “Module_data”, “type”: “file”, “format”: “json” }
def create_dictionaries(inputLines):
    if inputLines is None:
        return None

    paragraphsDict = {}
    dictionaryFiles = {}

    for x in range(0, len(inputLines), 3):
        if inputLines[x].startswith("## Begin"):
            paragraphHeader = re.match('(Paragraph...?)', inputLines[x].partition("Begin ")[2])
            inputLines[x + 1] = "name=" + inputLines[x + 1]
            for i in range(0, len(inputLines[x + 1].split(" "))):
                dictionaryFiles[inputLines[x + 1].replace("\n", "").split(" ")[i].split("=")[0]] = \
                    inputLines[x + 1].replace("\n", "").split(" ")[i].split("=")[1]

            paragraphsDict[paragraphHeader.group(0).replace("P", "p")] = dictionaryFiles.copy()

    return paragraphsDict


# 4. С опция създайте json или csv изходен файл съдържащ данните от речника
def main():
    parser = argparse.ArgumentParser(
        description="Convert to JSON, CSV or both")

    parser.add_argument("--path", type=str)
    parser.add_argument("--format", type=str)
    parser.add_argument("--output", type=str)

    args = parser.parse_args()

    file = args.path
    option = args.format
    output = args.output

    if file is None:
        file = "text_sample.txt"

    if option is None:
        option = "both"
        # change to 'csv' or 'json' if you want only one of them to be created, not 'both'.

    if output is None:
        output = "result"
        # the name of the csv or json file.

    while 1:
        if option.lower() == "csv":
            csv_convert.output_file(create_dictionaries(read_and_open_file(file)), output)
            break
        elif option.lower() == "json":
            json_convert.output_file(create_dictionaries(read_and_open_file(file)), output)
            break
        elif option.lower() == "both":
            dictList = create_dictionaries(read_and_open_file(file))
            json_convert.output_file(dictList, output)
            csv_convert.output_file(dictList, output)
            break
        else:
            print("Try another command.")
            continue


if __name__ == "__main__":
    main()
