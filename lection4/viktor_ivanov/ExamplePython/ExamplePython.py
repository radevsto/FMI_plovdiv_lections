def print_exercise_header(n: str, isEnd: bool):
    if(not isEnd):
        print(f"Start of Exercise {n}\n")
    else:
        print(f"\nEnd of Exercise {n}\n")


#1.  В списък от числа притирайте само четните от 0 до 100.
 #   - Hint използвайте range()
print_exercise_header(1,False)

# Solution
# -----------------------------------------------------------------------------------
for x in range(0,101):
    if x % 2 == 0:
        print(x)

# -----------------------------------------------------------------------------------
print_exercise_header(1,True)

# 2.  В стринг намерете всички думи които завършват на ‘o’ и ‘t’
# string='Lorem ipsum dolor sit amet, consectetur adipiscing elit.  Vivamus
# mattis tempus suscipit.  Mauris efficitur interdum turpis, vitae varius nunc
# fringilla non.  Vestibulum malesuada fringilla tellus vel iaculis.  In
# vehicula gravida fermentum.  Vivamus ultrices lacinia pretium.  Mauris orci
# lectus, lacinia at placerat ut, aliquam at quam.  Donec condimentum feugiat
# arcu, ut consectetur tortor ornare id.  Vivamus et arcu nunc.  Morbi viverra
# quam id libero rutrum elementum.  Integer nibh eros, varius eu euismod ac,
# accumsan congue mauris.  Integer eu mattis dui.  Pellentesque volutpat
# vehicula ultrices.’
print_exercise_header(2, False)

# Solution
# -----------------------------------------------------------------------------------
inputString = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis tempus suscipit. Mauris efficitur interdum turpis, vitae varius nunc fringilla non. Vestibulum malesuada fringilla tellus vel iaculis. In vehicula gravida fermentum. Vivamus ultrices lacinia pretium. Mauris orci lectus, lacinia at placerat ut, aliquam at quam. Donec condimentum feugiat arcu, ut consectetur tortor ornare id. Vivamus et arcu nunc. Morbi viverra quam id libero rutrum elementum. Integer nibh eros, varius eu euismod ac, accumsan congue mauris. Integer eu mattis dui. Pellentesque volutpat vehicula ultrices."
words = inputString.split(' ')
filterCharacters = {'t', 'o'}

for word in words:
    for character in filterCharacters:
        if(word.endswith(character)):
            print(word)

# -----------------------------------------------------------------------------------
print_exercise_header(2,1)

#3.  От предходния стринг, направете dictionary къде:
#В зависимост броя на буквите прибавете към съответния ключ на речник.
#Пример:

  # dict['two'] = ['at', 'ac', 'eu' ...]
  # dict['three'] = ['sit', 'non' 'dui’ … ]
print_exercise_header(3,False)

# Solution
# -----------------------------------------------------------------------------------
#Automatic (Different format)
# duplicateWordsCount = {a:words.count(a) for a in words}
# print(duplicateWordsCount)

#Manual
duplicatesCountDict = {"one": set([]), "two": set([]), "three": set([])}

for word in words:
    if(words.count(word) == 1):
        duplicatesCountDict["one"].add(word)
    if(words.count(word) == 2):
        duplicatesCountDict["two"].add(word)
    if(words.count(word) == 3):
        duplicatesCountDict["three"].add(word)

print(duplicatesCountDict)

# -----------------------------------------------------------------------------------
print_exercise_header(3,True)
