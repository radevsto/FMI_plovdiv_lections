import json
import csv
import os
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
def output_file(path: str, outputType: Enum=OutputType.ALL):
    input = get_dictionary_files(get_text_file_input(path))

    ## JSON File Write
    if outputType == OutputType.JSON or outputType == OutputType.ALL:
        print("\nJSON")
        print("******************")

        jsonOutput = json.dumps(input)
        try:
            with open("input.json", "w") as file_json:
                file_json.write(jsonOutput)
                print("Transformation Successful, JSON File Written")
        except:
            print("Could not complete JSON Transformation")
        finally:
            file_json.close()

    ## CSV File Write
    if outputType == OutputType.CSV or outputType == OutputType.ALL:
        print("\nCSV")
        print("******************")
        
        try:
            with open("input.csv", "w", newline="") as file_csv:
                file_csv.write("|")

                # Headers
                for paragraph in input[0].values():
                    for header in paragraph:
                        for key in header.keys():
                            file_csv.write(f"|{key}")

                file_csv.write("\n")

                # Content (The reason for using a string here is to remove the last character in the file with relative ease)
                contentString = ""
                for paragraph in input:
                    for key in paragraph:
                        contentString += (f"|{key}")
                        for line in paragraph[key]:
                            for value in line.values():
                                 contentString += (f"|{value}")
                     
                        contentString += ("\n")

                file_csv.write(contentString[:-1])
                print("Transformation Successful, CSV File Written")
        except:
             print("Could not complete CSV Transformation")
        finally:
             file_csv.close()

output_file("input.txt")