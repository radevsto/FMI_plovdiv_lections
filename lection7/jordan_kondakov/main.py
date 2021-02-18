import itertools
import textwrap
import string
import json_output
import csv_output


def open_and_read_file(file):
    _file = open(file, "r")
    paragraphs = _file.read().split("\n")
    chars = list(string.ascii_uppercase)
    dict_structure = {}

    for index, paragraph in enumerate(paragraphs):
        if (len(chars) > index + 1):
            print("## Begin Paragraph %s\n%s\n## End Paragraph %s" %
                  (chars[index], paragraph, chars[index]))

        splitted_paragraph = paragraph.split()
        for _ in splitted_paragraph:
            key = "paragraph %s" % chars[index]

            dict_structure[key] = {
                "name": splitted_paragraph[0],
                "type": splitted_paragraph[1].split("=")[1],
                "format": splitted_paragraph[2].split("=")[1]
            }

    json_output.to_json(dict_structure)
    csv_output.to_csv(dict_structure)


def main():
    # I didn't understand the requirements for this exercise very well but here it is
    open_and_read_file("the_file.txt")


if __name__ == "__main__":
    main()
