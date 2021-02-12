import re
import json
import csv
from enum import Enum

class OutputType(Enum):
    CSV = 1
    JSON = 2
    ALL = 3

def get_text_file_input(path: str):
    file = open(path, "r")
    return file.readlines()

def get_dictionary_files(inputLines: str):
    paragraphDict = {"paragraph": dict()}
    paragraphs = []

    for x in range(0, len(inputLines), 3):
        if inputLines[x].startswith("## Begin"): 
            paragraphDict = {((inputLines[x].partition("Begin ")[2]).replace('\n', '')).replace('P', 'p'): (inputLines[x + 1].replace('\n','').split(' '))}

        paragraphs.append(paragraphDict)
    
    for paragraph in paragraphs:
        for key in paragraph:
            for _ in range(0, len(paragraph)):
                paragraph[key][0] = "name=" + paragraph[key][0]

                for i in range(0, len(paragraph[key])):
                    paragraph[key][i] = paragraph[key][i].split('=')
                    paragraph[key][i] = {paragraph[key][i][0]:paragraph[key][i][1]}

    print(paragraphs)
    return paragraphs

def output_file(outputType: Enum):
    input = get_dictionary_files(get_text_file_input("input.txt"))

    # JSON Solution
    if outputType == OutputType.JSON or outputType == OutputType.ALL:
        jsonInput = json.dumps(input)
        print("\nJSON")
        print("******************")
        try:
            with open("input.json", "w") as file_json:
                file_json.write(jsonInput)
                print("Transformation Successful, JSON File Written")
        except:
            print("Could not complete JSON Transformation")

    if outputType == OutputType.CSV or outputType == OutputType.ALL:
        print("\nCSV")
        print("******************")
        
    # CSV Solution does not work yet
    #keys = ["name", "type", "format"]
    #with open("input.csv", "w", newline = "") as output_file_csv:
    #    dict_writer = csv.DictWriter(output_file_csv, keys)
    #    dict_writer.writeheader()
    #    dict_writer.writerows(input)
        return

output_file(OutputType.ALL)