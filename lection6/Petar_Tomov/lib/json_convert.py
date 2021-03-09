import json


def output_file(inputFile: list, outputFile: str = "result"):
    if inputFile is None:
        return

    jsonOutput = json.dumps(inputFile)
    try:
        with open(f"{outputFile}.json", "w") as file_json:
            file_json.write(jsonOutput)
            print("JSON File has been written.")
    except:
        print("Could not write JSON file.")
    finally:
        file_json.close()
