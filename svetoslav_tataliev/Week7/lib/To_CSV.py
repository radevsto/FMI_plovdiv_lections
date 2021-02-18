import csv


def create_row(dic: dict, header):
    row = [header, dic["name"], dic["type"], dic["format"]]

    return row


def create_csv(dic: dict):
    all_rows = []
    with open('CSV_Output.csv', 'w', newline='') as file:
        w = csv.writer(file, delimiter='|')
        for i in dic:
            all_rows.append(create_row(dic[i], i))
        w.writerow(['paragraph', 'name', 'type', 'format'])
        for rows in all_rows:
            w.writerow(rows)