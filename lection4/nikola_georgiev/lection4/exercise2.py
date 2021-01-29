#all the words which ends at 'o' or 't'
import re

string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer tempus semper orci, at maximus orci eleifend sed. Cras in elit fringilla, congue tellus a, convallis nulla. Ut at felis erat. Pellentesque consequat nibh ut nulla cursus sollicitudin. Pellentesque a viverra augue. Maecenas fermentum euismod mauris eu tristique. Nam erat sem, condimentum nec pharetra eget, mollis non sapien.Phasellus nec viverra orci. Morbi dapibus pretium hendrerit. Fusce porttitor lorem et sapien mollis blandit. Quisque ac justo bibendum, mattis urna eu, pellentesque leo. Nam aliquet dolor mauris, id dapibus diam condimentum a. Sed id dolor magna. Maecenas sodales, tellus sit amet efficitur condimentum, nibh ipsum consectetur augue, vitae tristique lacus turpis quis enim. Nam tincidunt elit metus, vitae varius nulla faucibus et. Pellentesque bibendum aliquam nunc ut tincidunt. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nam ut libero lacus. Aenean nisi ante, ullamcorper ac purus id, gravida suscipit mi. Integer pretium commodo ligula, ac mollis lorem vestibulum sit amet.'
listSpecialWords = []
for word in re.findall(r"[\w']+", string):
    if word[-1] == 'o' or word[-1] == 't':
        listSpecialWords.append(word)


print('Words that ends at o or t: ', listSpecialWords)

#dictionaries which divides by the numbers of letters in the words
listTwoLetters = []
listThreeLetters = []
for word in re.findall(r"[\w']+", string):
    if len(word) == 2:
        listTwoLetters.append(word)
    elif len(word) == 3:
        listThreeLetters.append(word)

dict ={}
dict['two'] = listTwoLetters
dict['three'] = listThreeLetters

for key, value in dict.items():
    print(key, value)
