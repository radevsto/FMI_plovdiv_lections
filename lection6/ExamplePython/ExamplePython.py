import re
import argparse
from lib import JsonConverter
from lib import CSVConverter

## Exercise

#Направете програма, която от файл подаден
#като аргумент прави следното:
#Отваря и прочита файла.
#Процесва файла на параграфи. Всеки параграх
#започва с ## Begin и завършва с ## End
#За всеки параграф направете dictionary
#структуора която има следната структура
#{ “paragraph A”: { “name”: “Module_data”,
#“type”: “file”,
#“format”: “json”
#}
#4. С опция създайте json или csv изходен файл
#съдържащ данните от речника

# Read all lines from a text file (Task #1)
def get_text_file_input(path: str):
    try:
        with open(path, "r") as file:
            return file.readlines()
    except:
        print("Could not locate file")

# Transformation of the Text File into Dictionary Files (Task #2 and Task #3)
def get_dictionary_files(inputLines: str):
    if inputLines == None:
        return None

    paragraphsDict = {}
    dictionaryFiles = {}

    for x in range(0, len(inputLines), 3):
        if inputLines[x].startswith("## Begin"):
            paragraphHeader = re.match('(Paragraph...?)', inputLines[x].partition("Begin ")[2])
            inputLines[x+1] = "name=" + inputLines[x+1]
            for i in range(0,len(inputLines[x+1].split(" "))):
                dictionaryFiles[inputLines[x+1].replace("\n","").split(" ")[i].split("=")[0]] = inputLines[x+1].replace("\n","").split(" ")[i].split("=")[1]

            paragraphsDict[paragraphHeader.group(0).replace("P", "p")] = dictionaryFiles.copy()
            
    print(paragraphsDict)            
    return paragraphsDict

# Conversion of Text File Content into JSON and CSV Files (Task #4)
def main():
    parser = argparse.ArgumentParser(description="A small application to convert a formatted Text File to a CSV or JSON file")

    parser.add_argument("--path", type = str,help = "Path for the file (By default, it's set as input.txt)")
    parser.add_argument("--format", type = str, help = "Output Input File to JSON, CSV or BOTH")
    parser.add_argument("--output", type = str, help = "Name of the Output text file for CSV and JSON")

    args = parser.parse_args()

    file = args.path
    option = args.format
    output = args.output

    if file is None:
        file = "input.txt"
    
    if option is None:
        option = "all"
    
    if output is None:
        output = "result"
    
    while(1):
        if option.lower() == "csv":
            CSVConverter.output_file(get_dictionary_files(get_text_file_input(file)), output)
            break
        elif option.lower() == "json":
            JsonConverter.output_file(get_dictionary_files(get_text_file_input(file)), output)
            break
        elif option.lower() == "all":
            dictList = get_dictionary_files(get_text_file_input(file))
            JsonConverter.output_file(dictList, output)
            CSVConverter.output_file(dictList, output)
            break
        else:
            print("Unrecognised option, please try again")
            continue


if __name__ == "__main__":
    main()
