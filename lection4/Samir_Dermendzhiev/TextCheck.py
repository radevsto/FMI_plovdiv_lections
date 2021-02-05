text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis tempus suscipit. " +
        "Mauris efficitur interdum turpis, vitae varius nunc fringilla non. Vestibulum malesuada " +
        "fringilla tellus vel iaculis. In vehicula gravida fermentum. Vivamus ultrices lacinia pretium. " +
        "Mauris orci lectus, lacinia at placerat ut, aliquam at quam. Donec condimentum feugiat arcu, " +
        "ut consectetur tortor ornare id. Vivamus et arcu nunc. Morbi viverra quam id libero rutrum elementum." +
        " Integer nibh eros, varius eu euismod ac, accumsan congue mauris. Integer eu mattis dui. " +
        "Pellentesque volutpat vehicula ultrices.")

text = text.replace('.', '')
text = text.replace(',', '')

words = text.split()

for word in words:
    if word.endswith('o') or word.endswith('t'):
        print(word)

occurrences = {}
for word in words:
    occurrences.setdefault(len(word), []).append(word)

# for word in occurrences:
#     print(occurrences[word])

print(occurrences)
# Условието на задачата е резултата да има следния формат:
# dict['two'] = ['at', 'ac', 'eu' ...]
# dict['three'] = ['sit', 'non' 'dui’ … ]
# Генерирания от вас дикт има следния:
# dict[2] = ['at', 'ac', 'eu' ...]
# dict[3] = ['sit', 'non' 'dui’ … ]
