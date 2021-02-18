import argparse
import re
from lib import csv_helper
from lib import json_helper

#Направете програма, която от файл подаден
#като аргумент прави следното:
#1. Отваря и прочита файла.
#2. Процесва файла на параграфи. Всеки параграх
#започва с ## Begin и завършва с ## End
#3. За всеки параграф направете dictionary
#структуора която има следната структура
#{ “paragraph A”: { “name”: “Module_data”,
#“type”: “file”,
#“format”: “json”
#}
#4. С опция създайте json или csv изходен файл
#съдържащ данните от речника


#store all paragraphs
paragraphs = dict()

class Paragraph:
    def __init__(self):
        self._paragraph_name = None
        self.name = None
        self.type = None
        self.format = None

    @property
    def paragraph_name(self):
        return self._paragraph_name

    @paragraph_name.setter
    def paragraph_name(self, value):
        self._paragraph_name = "paragraph " + value


#(!) Отваря и прочита файла. [Task 1]
def get_file_text(path):
    text = open(path, "r").read()
    #remove white spaces
    text = text.replace("\n", " ")

    return text

#(!) Процесва файла на параграфи. [Task 2]
#(!) За всеки параграф направете dictionary структуора [Task 3]
def extract_all_paragraphs(file_text):
    pattern = re.compile(r'## Begin Paragraph(.+?)##')
    matches = pattern.findall(file_text)

    for match in matches:
        match = match.replace("  ", " ")
        inner_pattern = re.compile(r'(\w+)\s(\w+)\stype=(\w+)\sformat=(\w+)')
        inner_matches = inner_pattern.search(match)

        p = Paragraph()
        p.paragraph_name = inner_matches.group(1)
        p.name = inner_matches.group(2)
        p.style = inner_matches.group(3)
        p.format = inner_matches.group(4)

        paragraphs[p.paragraph_name] = {"name": p.name,
                                        "type": p.style,
                                        "format": p.format}


def main():
    parser = argparse.ArgumentParser(description='Enter file path.')
    parser.add_argument('file_path', help="File path for input data")
    parser.add_argument('output_format', help="Output file format csv or json")

    args = parser.parse_args()

    file_path = args.file_path
    output_format = args.output_format

    #stop execution if output format is not valid
    if (output_format != "csv") & (output_format != "json"):
        return

    file_content = get_file_text(file_path)
    extract_all_paragraphs(file_content)

    # (!) С опция създайте json или csv изходен файл
    # съдържащ данните от речника [Task 4]
    if output_format == "csv":
        csv_helper.write_to_file(paragraphs)
    else:
        json_helper.write_to_file(paragraphs)


if __name__ == "__main__":
    main()
