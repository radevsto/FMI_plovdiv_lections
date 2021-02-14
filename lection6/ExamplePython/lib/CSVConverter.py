def output_file(input: list, output: str = "result"):
    if input == None:
        return
    
    print("\nCSV")
    print("******************")
    
    # CSV File Write
    try:
        with open(f"{output}.csv", "w", newline="") as file_csv:   
            file_csv.write("|") 

            # Headers
            for headers in input["paragraph A"]:
                file_csv.write(f"|{headers}")

            file_csv.write("\n")

            # Content (The reason for using a string here is to remove the last character in the file with relative ease)
            contentString = ""
            for paragraph in input:
                contentString += (f"|{paragraph}")
                for value in input[paragraph].values():
                    contentString += (f"|{value}")
                contentString += ("\n")

            file_csv.write(contentString[:-1])
            print("Transformation Successful, CSV File Written")
    except:
            print("Could not complete CSV Transformation")
    finally:
            file_csv.close()