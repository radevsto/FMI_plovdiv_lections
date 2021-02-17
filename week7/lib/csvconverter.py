import csv


def convert_to_csv(output_data, paragraph, name, file_type, file_format):
    csv_row = [paragraph, name, file_type, file_format]
    output_data.append(csv_row)


def write_to_csv(data):
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(['paragraph', 'name', 'type', 'format'])
        for row in data:
            writer.writerow(row)
