from util import string_to_words_list
from num2words import num2words
from word2number import w2n


def string_to_dictionary_word_letters_count_words(string):
    words = string_to_words_list(string)
    word_letters_count_words = {}
    for word in words:
        key = num2words(len(word))
        if key not in word_letters_count_words:
            word_letters_count_words[key] = []
        word_letters_count_words[key].append(word)
    return word_letters_count_words


def string_to_dictionary_word_letters_count_characters(string):
    word_letters_count_words = string_to_dictionary_word_letters_count_words(string)
    word_letters_count_all_characters_count = {k: len(v) * w2n.word_to_num(k) for (k, v) in
                                               word_letters_count_words.items()}
    return word_letters_count_all_characters_count


def print_word_letters_count_words(string):
    word_letters_count_words = string_to_dictionary_word_letters_count_words(string)
    print("-----\nDictionary of letters count for word as a key and all words with the same letters count:\n-----")
    for key in word_letters_count_words:
        print("KEY: " + key)
        print(word_letters_count_words[key])
    print("-----\nEND\n-----")


def print_word_letters_count_characters(string):
    word_letters_count_all_characters_count = string_to_dictionary_word_letters_count_characters(string)
    print("-----\nDictionary comprehension:\n-----")
    for key in word_letters_count_all_characters_count:
        print("KEY: " + key)
        print(word_letters_count_all_characters_count[key])
    print("-----\nEND\n-----")
