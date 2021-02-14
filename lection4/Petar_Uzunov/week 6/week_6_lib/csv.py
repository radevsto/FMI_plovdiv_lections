def format(data):
    finalData = '|'

    # creates the header row with the given attributes
    for value in data[0].values():
        for subvalue in value.keys():
            finalData += '|' + subvalue                     # name, type, format
        break
    finalData += '\n'

    for item in data:
        for key in item.keys():
            finalData += '|' + key                          # key = paragraph (A-Z)
            for subvalue in item.values():                  # subvalue = {'name': '...', 'type': '...', ...}
                for subkey in subvalue.keys():              # subkey = 'name', 'type', ...
                    finalData += '|' + subvalue[subkey]
            finalData += '\n'

    # saves the output to 'dump.txt'
    with open('./dump.txt', 'w') as file:
        file.write(finalData)
        file.close()

    return finalData