import csv


def write_to_file(val: dict):
    with open('csv_output.csv', 'w', newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONE, delimiter="|")

        writer.writerow(["", "", "name", "type", "format"])

        for key, value in val.items():
            row = ["", key]
            for k, v in value.items():
                row.append(v)
            writer.writerow(row)

