import re
from json_output import print_json
import argparse
from csv_output import print_csv







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f')
    args = parser.parse_args(['-f', 'input.txt'])
    arr = []
    dict1 = {}
    with open(args.f, "r") as fh:
        for line in fh:
            elements = re.split("\\W+", line)
            if elements[1] == 'Begin':
                element = re.split("^\\W+\\s+[a-zA-Z]+\\s+", line, 1)
                paragraph = element[1].strip()
                # print(paragraph)
            elif elements[1] == 'End':
                paragraph = ''
            else:
                description_json = {'name': elements[0], elements[1]: elements[2], elements[3]: elements[4]}
                arr.append({'': paragraph, 'name': elements[0], elements[1]: elements[2], elements[3]: elements[4]})
                dict1[paragraph] = description_json

    print_json(dict1)
    print_csv(arr)
