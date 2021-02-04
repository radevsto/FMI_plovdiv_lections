import re
from num2words import num2words
from word2number import w2n

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis tempus suscipit. " \
       "Mauris efficitur interdum turpis, vitae varius nunc fringilla non. Vestibulum malesuada fringilla " \
       "tellus vel iaculis. In vehicula gravida fermentum. Vivamus ultrices lacinia pretium. Mauris orci lectus, " \
       "lacinia at placerat ut, aliquam at quam. Donec condimentum feugiat arcu, ut consectetur tortor ornare id. " \
       "Vivamus et arcu nunc. Morbi viverra quam id libero rutrum elementum. Integer nibh eros, " \
       "varius eu euismod ac, accumsan congue mauris. Integer eu mattis dui. Pellentesque volutpat vehicula ultrices."

words = re.split(r'[,.\s]\s*', text)
word_count = {}

for word in words:
    num_word = num2words(len(word))
    if num_word not in word_count.keys():
        word_count[num_word] = []
        word_count[num_word].append(word)
    else:
        word_count[num_word].append(word)

print('Word length -> words of each length:')
for wordLength, words in word_count.items():
    print(f'{wordLength} -> {words}')

word_count_comprehension = {k: len(v)*w2n.word_to_num(k) for (k, v) in word_count.items()}

print('\nWord length -> total letter count:')
for wordLength, totalLetterCount in word_count_comprehension.items():
    print(f'{wordLength} -> {totalLetterCount}')
