from first_task import print_even_numbers
from second_task import all_words_ending_in
from third_task import print_word_letters_count_words, print_word_letters_count_characters

string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis tempus suscipit. Mauris" \
             "efficitur interdum turpis, vitae varius nunc fringilla non. Vestibulum malesuada fringilla tellus vel" \
             "iaculis. In vehicula gravida fermentum. Vivamus ultrices lacinia pretium. Mauris orci lectus, lacinia" \
             "at placerat ut, aliquam at quam. Donec condimentum feugiat arcu, ut consectetur tortor ornare id." \
             "Vivamus et arcu nunc. Morbi viverra quam id libero rutrum elementum. Integer nibh eros, varius eu" \
             "euismod ac, accumsan congue mauris. Integer eu mattis dui. Pellentesque volutpat vehicula ultrices."
print_even_numbers()
all_words_ending_in(string, 't')
all_words_ending_in(string, 'o')
print_word_letters_count_words(string)
print_word_letters_count_characters(string)
