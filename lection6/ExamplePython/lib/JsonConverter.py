import json

def output_file(input: list, output: str = "result"):
      if input == None:
          return

      print("\nJSON")
      print("******************")

      # JSON File Write
      jsonOutput = json.dumps(input)
      try:
          with open(f"{output}.json", "w") as file_json:
              file_json.write(jsonOutput)
              print("Transformation Successful, JSON File Written")
      except:
          print("Could not complete JSON Transformation")
      finally:
          file_json.close()