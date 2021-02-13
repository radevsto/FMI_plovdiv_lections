import json

def output_file(input: list):
      if input == None:
          return

    ## JSON File Write
      print("\nJSON")
      print("******************")

      jsonOutput = json.dumps(input)
      try:
          with open("input.json", "w") as file_json:
              file_json.write(jsonOutput)
              print("Transformation Successful, JSON File Written")
      except:
          print("Could not complete JSON Transformation")
      finally:
          file_json.close()