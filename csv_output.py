import csv

def print_csv(dict_csv):
    try:
        with open('output.csv', 'w',  newline='') as new_file:
            fieldnames = ['', 'name', 'type', 'format']
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='|', quotechar='1')
            csv_writer.writeheader()
            for data in dict_csv:
                csv_writer.writerow(data)
    except IOError:
        print("I/O error")