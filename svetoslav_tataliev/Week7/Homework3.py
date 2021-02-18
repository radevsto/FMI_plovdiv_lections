import re
import argparse

from lib import To_JSON
from lib import To_CSV


def read_file(path):
    main_dictionary = {}
    my_file = open(path, 'r').read().replace("## Begin ", "")
    text = re.sub(r'## End .*', "", my_file).split("\n\n")
    for i in range(len(text)):
        dic = {(text[i].splitlines()[0]): create_sub_dic(text[i].splitlines()[1])}
        merge_dic(main_dictionary, dic)
    return main_dictionary


def create_sub_dic(string):
    dic = {"name": "",
           "type": "",
           "format": ""
           }
    content = string.split()
    dic.update({"name": content[0]})
    dic.update({"type": content[1][5:]})
    dic.update({"format": content[2][7:]})
    return dic


def merge_dic(dic1: dict, dic2: dict):
    return dic1.update(dic2)


def output():
    parser = argparse.ArgumentParser(description='Choose what type of format you what the file to be converted to.')
    parser.add_argument('path', type=str, help='Path of the file')
    parser.add_argument('type', type=str, choices=['csv', 'json'])
    args = parser.parse_args()
    dic = read_file(args.path)
    if args.type == "csv":
        To_CSV.create_csv(dic)
    elif args.type == "json":
        To_JSON.create_json(dic)
    else:
        To_CSV.create_csv(dic)
        To_JSON.create_json(dic)


if __name__ == '__main__':
    output()

