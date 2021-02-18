import argparse
import csv
import os
import re


def formatFileCSV(path: str):
    if not os.path.exists(path):
        print("File Could Not Be Found!")
        return
    dicList = dict()
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    listData = list()
    iterator = iter(lines)
    for el in iterator:
        if el.startswith("## Begin"):
            listData.append(el + " " + next(iterator) + next(iterator))

    for el in listData:
        result = re.search('## Begin Paragraph(.*)## End Paragraph', el)
        info = result.group(1)
        inWords = info.split(" ")
        tempDictionary = {
            "name": inWords[2],
            "type": inWords[3].removeprefix("type="),
            "format": inWords[4].removeprefix("format=")
        }
        dicList["Paragraph " + inWords[1]] = tempDictionary
        with open(os.path.dirname(path) + "\ " + os.path.basename(path).split(".")[0] + ".csv", 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter="|")
            paragraphs = sorted(list(dicList.values())[0].keys())
            for key in dicList.keys():
                writer.writerow([key] + [dicList[key][paragraph] for paragraph in paragraphs])
        print("CSV File Created Successfully!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.set_defaults(method=formatFileCSV)
    parser.add_argument('path', type=str)
    arguments = parser.parse_args()
    arguments.method(**vars(arguments))
