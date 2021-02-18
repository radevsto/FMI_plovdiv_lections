import re

# 1 - return all even numbers from 0 to 100
arr = []

for i in range(0, 101):
    if i % 2 == 0:
        arr.append(i)

print(arr)
print()

# 2 - return all words from a string that end with the letters 'o' and 't'
string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis tempus suscipit. Mauris efficitur interdum turpis, vitae varius nunc fringilla non. Vestibulum malesuada fringilla tellus vel iaculis. In vehicula gravida fermentum. Vivamus ultrices lacinia pretium. Mauris orci lectus, lacinia at placerat ut, aliquam at quam. Donec condimentum feugiat arcu, ut consectetur tortor ornare id. Vivamus et arcu nunc. Morbi viverra quam id libero rutrum elementum. Integer nibh eros, varius eu euismod ac, accumsan congue mauris. Integer eu mattis dui. Pellentesque volutpat vehicula ultrices.'

string = re.sub(r'\W+', ' ', string)

strArr = []

for i in string.split():
    if i[-1] == 'o' or i[-1] == 't':
        strArr.append(i)

print(strArr)
print()

# 3 - arrange all words from a string with the same length in separate dictionary properties (keys)
numbersStrings = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
}

stringsDict = {}

for i in numbersStrings:
    stringsDict[numbersStrings[i]] = []

for i in string.split():
    if len(i) <= 10:
        stringsDict[numbersStrings[len(i)]].append(i)

for i in stringsDict:
    print(f'{i}: {stringsDict[i]}')

print()


# 4 - get the total number of letters from every dictionary key


def get_key(value, dictionary):
    for k, v in dictionary.items():
        if value == v:
            return k

    return 0


numDict = {k: len(v) * get_key(k, numbersStrings) for (k, v) in stringsDict.items()}

print(numDict)
