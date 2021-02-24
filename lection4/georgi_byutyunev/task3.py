import re
from num2words import num2words

string='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis tempus suscipit. Mauris efficitur interdum turpis, vitae varius nunc fringilla non. Vestibulum malesuada fringilla tellus vel iaculis. In vehicula gravida fermentum. Vivamus ultrices lacinia pretium. Mauris orci lectus, lacinia at placerat ut, aliquam at quam. Donec condimentum feugiat arcu, ut consectetur tortor ornare id. Vivamus et arcu nunc. Morbi viverra quam id libero rutrum elementum. Integer nibh eros, varius eu euismod ac, accumsan congue mauris. Integer eu mattis dui. Pellentesque volutpat vehicula ultrices.'
words = re.split('[ ,.!?-]', string)
words = filter(None, words)

dictionary = {}

for word in words:
    numberString = num2words(len(word))
    if numberString not in dictionary:
        dictionary[numberString]=[]
    dictionary[numberString].append(word)

for key in dictionary:
    print(f'{key} - {len(dictionary[key][0]) * len(dictionary[key])} - {dictionary[key]}')