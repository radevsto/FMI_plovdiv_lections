lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis tempus suscipit. Mauris efficitur' \
         ' interdum turpis, vitae varius nunc fringilla non. Vestibulum malesuada fringilla tellus vel iaculis.' \
         ' In vehicula gravida fermentum. Vivamus ultrices lacinia pretium. Mauris orci lectus, lacinia at placerat ut, ' \
         'aliquam at quam. Donec condimentum feugiat arcu, ut consectetur tortor ornare id. Vivamus et arcu nunc. Morbi' \
         ' viverra quam id libero rutrum elementum. Integer nibh eros, varius eu euismod ac, accumsan congue mauris.' \
         ' Integer eu mattis dui. Pellentesque volutpat vehicula ultrices."


def print_even():
    for number in range(100):
        if number % 2 == 0:
            print(number)


def search_final_letters():

    str_replace_commas = lorem.replace(',', '')
    str_replace_dots = str_replace_commas.replace('.', '')
    spliced_string = str_replace_dots.split()
    for word in spliced_string:
        if word.endswith('o') or word.endswith('t'):
            print(word)


def find_sum():
    str_replace_commas = lorem.replace(',', '')
    str_replace_dots = str_replace_commas.replace('.', '')
    str_replace_apostrophe = str_replace_dots.replace("'", '')
    spliced_string = str_replace_apostrophe.split()
    number_of_letters = {}
    for word in spliced_string:
        length = len(word)
        if length not in number_of_letters:
            number_of_letters[length] = []
        number_of_letters[length].append(word)

    for key in number_of_letters:
        sum = len(number_of_letters[key]) * key
        print('Key %d - Sum %d' % (key, sum))


print_even()
print()
search_final_letters()
print()
find_sum()

