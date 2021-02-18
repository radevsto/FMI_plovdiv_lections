import csv


def to_csv(dict_structure):
    data = [["", "name", "type", "format"]]
    for key, value in dict_structure.items():
        data.append([key, value["name"], value["type"], value["format"]])

    csv_file = open("csv_formated_file.csv", "w+")
    writer = csv.writer(csv_file, delimiter='|')
    writer.writerows(data)
    csv_file.close()
