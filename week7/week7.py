import argparse
import re
from lib import csvconverter
from lib import jsonconverter


def parse_data(args, output_data, output_type):
    pattern = re.compile('(?<=Begin ).*?(?=E)')
    args_str = pattern.finditer(
        ''.join([str(elem) for elem in args.file.readlines()]).replace('\n', ' ').replace('#', ''))

    for match in args_str:
        row = match.group().split()
        paragraph = f"{row[0]} {row[1]}"
        name = row[2]
        file_type = row[3][5:]
        file_format = row[4][7:]
        if output_type.lower() == "json":
            jsonconverter.convert_to_json(output_data, paragraph, name, file_type, file_format)
            jsonconverter.write_to_json(output_data)
        elif output_type.lower() == "csv":
            csvconverter.convert_to_csv(output_data, paragraph, name, file_type, file_format)
            csvconverter.write_to_csv(output_data)


def main():
    json_data = {}
    csv_data = []

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--file',
        help='Input file',
        type=argparse.FileType('r'),
    )
    parser.add_argument(
        '-o', '--output',
        help='output file type [json/csv]',
        type=str
    )

    args = parser.parse_args()

    if args.output == "csv":
        parse_data(args, csv_data, "csv")
    elif args.output == "json":
        parse_data(args, json_data, "json")
    else:
        parse_data(args, csv_data, "csv")
        parse_data(args, json_data, "json")


if __name__ == "__main__":
    main()
