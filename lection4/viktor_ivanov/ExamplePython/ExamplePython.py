## Preparation Functions
def print_exercise_header(n: str, isEnd: bool):
    if(not isEnd):
        print(f"Start of Exercise {n}\n")
    else:
        print(f"\nEnd of Exercise {n}\n")

# Number-To-Word Solution taken from StackOverflow: https://stackoverflow.com/a/24123028
def as_words(n):
    # Convert an integer n (+ve or -ve) to English words.
    # lookups
    ones = ['zero', 'one', 'two', 'three', 'four',
            'five', 'six', 'seven', 'eight', 'nine', 
            'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
            'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['zero', 'ten', 'twenty', 'thirty', 'forty',
            'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    # negative case
    if n < 0:
        return "minus {0}".format(as_words(abs(n)))
    # 1000+
    for order, word in [(10 ** 12, "trillion"), (10 ** 9, "billion"),
                        (10 ** 6, "million"), (10 ** 3, "thousand")]:
        if n >= order:
            return "{0} {1}{2}".format(as_words(n // order), word,
                                       " {0}".format(as_words(n % order))
                                       if n % order else "")
    # 100-999
    if n >= 100:
        if n % 100:
            return "{0} hundred and {1}".format(as_words(n // 100), 
                                                as_words(n % 100))
        else:
            return "{0} hundred".format(as_words(n // 100))
    # 0-99
    if n < 20:
        return ones[n]
    else:
        return "{0}{1}".format(tens[n // 10],
                               "-{0}".format(as_words(n % 10)) 
                               if n % 10 else "")   

## Exercises

 # 1.  В списък от числа притирайте само четните от 0 до 100.
 #   - Hint използвайте range()

print_exercise_header(1,False)

# Solution
# -----------------------------------------------------------------------------------

for x in range(0, 101, 2):
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

inputString = inputString.replace(",", "")
inputString = inputString.replace(".", "")

words = inputString.split(' ')
filterCharacters = {'t', 'o'}

for word in words:
    for character in filterCharacters:
        if(word.endswith(character)):
            print(word)

# -----------------------------------------------------------------------------------
print_exercise_header(2,True)

# 3.  От предходния стринг, направете dictionary къде:
# В зависимост броя на буквите прибавете към съответния ключ на речник.
# Пример:

  # dict['two'] = ['at', 'ac', 'eu' ...]
  # dict['three'] = ['sit', 'non' 'dui’ … ]

print_exercise_header(3,False)

# Solution
# -----------------------------------------------------------------------------------

# Automatic

duplicateWordsCount = {a: words.count(a) for a in words}
maxDuplicateCount = max(duplicateWordsCount.values())
newDuplicateDict = {"one": set([])}

for x in range(1, maxDuplicateCount + 1):
    newDuplicateDict[as_words(x)] = set([])
    for word in words:
        if (words.count(word) == x):
            newDuplicateDict[as_words(x)].add(word)

newDuplicateDictCount = {word: len(word) * len(newDuplicateDict[word]) for word in newDuplicateDict}

print(f"{newDuplicateDict}\n")
print(newDuplicateDictCount)

# Manual

#duplicatesCountDict = {"one": set([]), "two": set([]), "three": set([])}

#for word in words:
#    if(words.count(word) == 1):
#        duplicatesCountDict["one"].add(word)
#    if(words.count(word) == 2):
#        duplicatesCountDict["two"].add(word)
#    if(words.count(word) == 3):
#        duplicatesCountDict["three"].add(word)

#duplicateDictCount = {word: len(str(word)) * len(duplicatesCountDict[word]) for word in duplicatesCountDict}

#print(duplicatesCountDict)
#print(duplicateDictCount)

# -----------------------------------------------------------------------------------
print_exercise_header(3,True)