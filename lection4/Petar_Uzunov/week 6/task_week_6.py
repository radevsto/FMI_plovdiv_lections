import argparse
import sys
import re
import week_6_lib

# program is started with args './source.txt' <'csv' or 'json'>

# adds the args
def load_args():
    parser = argparse.ArgumentParser(usage='week 6 task', description='week 6 task')
    parser.add_argument('file')
    parser.add_argument('format')
    args = parser.parse_args()
    return args

# reads file source.txt and returns a list of dictionaries with each paragraph
# each dictionary has 1 key 'paragraph [A-Z]' and another dictionary with keys 'name', 'type', 'format' as its value
def convert_file(path, format):
    paragraphs = []
    with open(path) as file:
        content = file.read()

        # using re.findall() to get all the matches
        # will result in a list of tuples
        list = re.findall('(## Begin Paragraph [A-Z])\n([A-Z _ a-z]+) (type)=([a-z _]+) (format)=([a-z]+)\n(## End Paragraph [A-Z])', content)
                           #            0                   1           2        3          4       5               6
        for i in range(0, len(list)):
            # ## Begin Paragraph [A-Z] -> first element of the tuple inside the list
            # 0    1       2       3   -> indexes of the list made by split()
            index = str.format('{}', list[i][0]).split(' ')[3] 
            paragraphName = list[i][1]
            type = list[i][3]
            format = list[i][5]

            # formats the string with the data and adds it to the output list
            paragraphs.append({
                str.format('paragraph {}', index):
                    {
                        'name': paragraphName,
                        'type': type,
                        'format': format
                    }
                })
        file.close()
        if('json' == format):
            json_formatter.format(paragraphs)
        elif('csv' == format):
            csv_formatter.format(paragraphs)


args = load_args()
convert_file(args.file, args.format)
