def output_file(input: list):
    if input == None:
        return

    print("\nCSV")
    print("******************")
        
    try:
        with open("input.csv", "w", newline="") as file_csv:
            file_csv.write("|")

            # Headers
            for paragraph in input[0].values():
                for header in paragraph:
                    for key in header.keys():
                        file_csv.write(f"|{key}")

            file_csv.write("\n")

            # Content (The reason for using a string here is to remove the last character in the file with relative ease)
            contentString = ""
            for paragraph in input:
                for key in paragraph:
                    contentString += (f"|{key}")
                    for line in paragraph[key]:
                        for value in line.values():
                                contentString += (f"|{value}")
                     
                    contentString += ("\n")

            file_csv.write(contentString[:-1])
            print("Transformation Successful, CSV File Written")
    except:
            print("Could not complete CSV Transformation")
    finally:
            file_csv.close()