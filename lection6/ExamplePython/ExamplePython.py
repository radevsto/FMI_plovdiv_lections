import json
import csv
from enum import Enum

class OutputType(Enum):
    CSV = 1
    JSON = 2
    ALL = 3

# Read all lines from a text file (Task #1)
def get_text_file_input(path: str):
    file = open(path, "r")
    return file.readlines()

#Transformation of the Text File into Dictionary Files (Task #2 and Task #3)
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

# Output the Dictionary files into .csv and .json files (Task #4)
def output_file(path: str, outputType: Enum = OutputType.ALL):
    input = get_dictionary_files(get_text_file_input(path))

    ## JSON File Write
    if outputType == OutputType.JSON or outputType == OutputType.ALL:
        jsonOutput = json.dumps(input)
        print("\nJSON")
        print("******************")
        try:
            with open("input.json", "w") as file_json:
                file_json.write(jsonOutput)
                print("Transformation Successful, JSON File Written")
        except:
            print("Could not complete JSON Transformation")

    if outputType == OutputType.CSV or outputType == OutputType.ALL:
        print("\nCSV")
        print("******************")
        
    ## CSV File Write
    # Automatic (does not work for now)
    #keys = ["name", "type", "format"]
    #with open("input.csv", "w", newline = "") as output_file_csv:
    #    dict_writer = csv.DictWriter(output_file_csv, keys)
    #    dict_writer.writeheader()
    #    dict_writer.writerows(input)

    # Manual
        keys = ["name", "type", "format"]
        with open("input.csv", "w", newline="") as file_csv:
            file_csv.write("|")
        # Headers
            for key in keys:
                file_csv.write(f"|{key}")

            file_csv.write("\n")

        #Content
            for paragraph in input:
                for key in paragraph:
                    file_csv.write(f"|{key}")
                    file_csv.write(f"|{paragraph[key][0]['name']}")
                    file_csv.write(f"|{paragraph[key][1]['type']}")
                    file_csv.write(f"|{paragraph[key][2]['format']}")
                    file_csv.write("\n")

            print("Transformation Successful, CSV File Written")


output_file("input.txt")