import argparse
import JsonConverter
import CSVConverter

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
        file = open(path, "r")
        return file.readlines()
    except:
        print("Could not locate file")

# Transformation of the Text File into Dictionary Files (Task #2 and Task #3)
def get_dictionary_files(inputLines: str):
    if inputLines == None:
        return None

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

    return paragraphs

def main():
    parser = argparse.ArgumentParser(description="Input Text File Path")

    parser.add_argument("--path", type = str,help = "Path for the file (By default, it's set as input.txt)")
    parser.add_argument("--format", type = str, help = "Output Input File to JSON, CSV or BOTH")

    args = parser.parse_args()

    file = args.path
    option = args.format

    if file is None:
        file = "input.txt"
    
    if option is None:
        option = "all"
    
    while(1):
        if option.lower() == "csv":
            CSVConverter.output_file(get_dictionary_files(get_text_file_input(file)))
            break
        elif option.lower() == "json":
            JsonConverter.output_file(get_dictionary_files(get_text_file_input(file)))
            break
        elif option.lower() == "all":
            dictList = get_dictionary_files(get_text_file_input(file))
            JsonConverter.output_file(dictList)
            CSVConverter.output_file(dictList)
            break
        else:
            print("Unrecognised option, please try again")
            continue


if __name__ == "__main__":
    main()
