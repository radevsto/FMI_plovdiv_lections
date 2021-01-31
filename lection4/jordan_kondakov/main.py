import re
import itertools


def main():
    # Exercise 1: Print all even numbers between 0 and 100
    # Starting from 2 because 0 is not an even number
    for number in range(2, 100, 2):
        print(number)

    # Exercise 2: Having the string below print all of the words that end with "o" or "t"
    # string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis tempus suscipit. Mauris
    # efficitur interdum turpis, vitae varius nunc fringilla non. Vestibulum malesuada fringilla tellus vel
    # iaculis. In vehicula gravida fermentum. Vivamus ultrices lacinia pretium. Mauris orci lectus, lacinia at
    # placerat ut, aliquam at quam. Donec condimentum feugiat arcu, ut consectetur tortor ornare id. Vivamus et
    # arcu nunc. Morbi viverra quam id libero rutrum elementum. Integer nibh eros, varius eu euismod ac, accumsan
    # congue mauris. Integer eu mattis dui. Pellentesque volutpat vehicula ultrices."""
    # print(re.findall(r'\b(\w+(o|t))\b', string))

    # Exercise 3: Having the string below create a dictionary that has:
    # 1) keys dependant on the count of the characters in a word
    # 2) using dictionary comprehension find the sum of each key
    # string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis tempus suscipit. Mauris
    # efficitur interdum turpis, vitae varius nunc fringilla non. Vestibulum malesuada fringilla tellus vel
    # iaculis. In vehicula gravida fermentum. Vivamus ultrices lacinia pretium. Mauris orci lectus, lacinia at
    # placerat ut, aliquam at quam. Donec condimentum feugiat arcu, ut consectetur tortor ornare id. Vivamus et
    # arcu nunc. Morbi viverra quam id libero rutrum elementum. Integer nibh eros, varius eu euismod ac, accumsan
    # congue mauris. Integer eu mattis dui. Pellentesque volutpat vehicula ultrices."""

    # # 1)
    # # the above string with no special characters
    # formated_string = re.sub('[^A-Za-z0-9]+', ' ', string)
    # sorted_string_by_words_length = sorted(
    #     formated_string.lower().split(), key=len)
    # desired_dict = {k: set(g)
    #                 for k, g in itertools.groupby(sorted_string_by_words_length, key=len)}
    # print(desired_dict)

    # # 2)
    # counter = 2
    # while counter <= len(desired_dict) + 1:
    #     key_values_sum = counter * len(desired_dict[counter])
    #     print('%s: %s' % (counter, key_values_sum))
    #     counter += 1


if __name__ == "__main__":
    main()
