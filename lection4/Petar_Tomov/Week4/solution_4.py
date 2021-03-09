# 1. В списък от числа принтирайте само четните от 0 до 100.
print("Task 1:")
for n in range(0, 101, 2):
    print(n)

# 2. В стринг намерете всички думи които завършват на ‘o’ и ‘t’
print("\nTask 2:")
inputString = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis tempus suscipit. Mauris ' \
              'efficitur interdum turpis, vitae varius nunc fringilla non. Vestibulum malesuada fringilla tellus vel ' \
              'iaculis. In vehicula gravida fermentum. Vivamus ultrices lacinia pretium. Mauris orci lectus, ' \
              'lacinia at placerat ut, aliquam at quam. Donec condimentum feugiat arcu, ut consectetur tortor ornare ' \
              'id. Vivamus et arcu nunc. Morbi viverra quam id libero rutrum elementum. Integer nibh eros, ' \
              'varius eu euismod ac, accumsan congue mauris. Integer eu mattis dui. Pellentesque volutpat vehicula ' \
              'ultrices. '
inputString = inputString.replace(",", "")
inputString = inputString.replace(".", "")
words = inputString.split(' ')
endingChar = {'o', 't'}
occur = {}
for word in words:
    for char in endingChar:
        if word.endswith(char):
            print(word)
    occur.setdefault(len(word), []).append(word)

# 3. От предходния стринг, направете dictionary къде: В зависимост броя на буквите прибавете към съответния ключ на
# речник. Пример: dict['two'] = ['at', 'ac', 'eu' ...] dict['three'] = ['sit', 'non' 'dui’ … ] Използвайки dictionary
# comprehension сумирайте тоталния брой на букви за всеки ключ. Тоест ако имаме две думи в ключ с 3 букви,
# общия брой е 6.
print("\nTask 3:")
print(occur)

