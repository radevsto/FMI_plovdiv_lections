import csv

def format(data):
    with open('dump.csv', 'w') as file:
        header = ['']
        for attr in data[0].values():
            for subattr in attr.keys():
                header.append(subattr)
        dump = csv.DictWriter(file, header, delimiter='|')
        dump.writeheader()
        new_dict = {}
        for item in data:
            for key in item.keys():
                new_dict[header[0]] = key
                for attr in header:
                    if attr == header[0]:
                       continue
                    new_dict[attr] = item[key][attr]
                dump.writerow(new_dict)
        file.close()
