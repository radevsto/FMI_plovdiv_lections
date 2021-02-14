def format(data):
    finalData = '{\n'
    for item in data:
        for key in item.keys():                                # key = paragraph (A-Z)
            finalData += '\t\"' + key + '\":\n\t\t{\n'                                               
            for subdict in item.values():                      # subdict = {'name': '...', 'type': '...', ...}
                for subkey in subdict.keys():                  # subkey = 'name', 'type', ...
                    finalData += '\t\t\t\"' + subkey + '": \"' + subdict[subkey] + '\",\n'
            finalData += '\t\t}\n'
    finalData += '}'

    # saves the output to 'dump.txt'
    with open('./dump.txt', 'w') as file:
        file.write(finalData)
        file.close()

    return finalData
