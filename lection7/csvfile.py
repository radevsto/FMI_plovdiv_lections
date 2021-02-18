import csv

def func(dict):
    with open('csvFile.csv', mode='w') as csv_file:
        fieldnames = ['', 'name', 'type', 'format']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='|')

        writer.writeheader()
        for data in dict:
            writer.writerow({field: dict[data].get(field) or data for field in fieldnames})
