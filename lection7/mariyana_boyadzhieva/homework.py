import argparse
import re
from lib.create_csv_file import dict_to_csv
from lib.create_json_file import dict_to_json

paragraphs_info = {}

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file_name", required=True)
parser.add_argument("-o", "--output_format", required=True)
args = parser.parse_args()


def read_file(file_name):
    file = open(file_name, 'r')
    lines = file.read()
    pattern = re.compile('(## Begin Paragraph [A-Z])\n\n([A-Z][a-z]+_data) (type)=([a-z_]+) (format)=([a-z]+)\n\n(## End Paragraph [A-Z])')
    matches = re.findall(pattern, lines)

    for line in matches:
        paragraph_name = line[0].split(" ")[2] + " " + line[0].split(" ")[3]
        info_data = line[1]
        paragraph_type = line[3]
        paragraph_format = line[5]

        paragraphs_info.update(
            {paragraph_name: {
                "name": info_data,
                line[2]: paragraph_type,
                line[4]: paragraph_format
            }}
        )

    file.close()


def create_output_file(output_format):
    if output_format == "csv":
        dict_to_csv(paragraphs_info)
    if output_format == "json":
        dict_to_json(paragraphs_info)


read_file(args.file_name)
create_output_file(args.output_format)
