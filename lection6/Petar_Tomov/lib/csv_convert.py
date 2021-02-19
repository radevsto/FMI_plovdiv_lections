def output_file(inputFile: list, outputFile: str = "result"):
    if inputFile is None:
        return

    try:
        with open(f"{outputFile}.csv", "w", newline="") as file_csv:
            file_csv.write("|")

            for headers in inputFile["paragraph A"]:
                file_csv.write(f"|{headers}")

            file_csv.write("\n")

            contentString = ""
            for paragraph in inputFile:
                contentString += f"|{paragraph}"
                for value in inputFile[paragraph].values():
                    contentString += f"|{value}"
                contentString += "\n"

            file_csv.write(contentString[:-1])
            print("CSV File has been written.")
    except:
        print("Could not write CSV file.")
    finally:
        file_csv.close()
