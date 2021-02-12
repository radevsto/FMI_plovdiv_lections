from util import string_to_words_list


def all_words_ending_in(string, character):
    counter = 0
    words = string_to_words_list(string)
    words_ending_in_character = []
    for word in words:
        if word[-1] == character:
            words_ending_in_character.append(word)
            counter += 1

    print("-----\nFound " + str(counter) + " words ending in " + character + ":\n-----")
    for word in words_ending_in_character:
        print(word)
    print("-----\nEND\n-----")
