import re
from math import sqrt

a = 100
for num in range(a+1):
     if num % 2:
         print(num)


string="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis tempus suscipit. Mauris efficitur interdum turpis, vitae varius nunc fringilla non. Vestibulum malesuada fringilla tellus vel iaculis. In vehicula gravida fermentum. Vivamus ultrices lacinia pretium. Mauris orci lectus, lacinia at placerat ut, aliquam at quam. Donec condimentum feugiat arcu, ut consectetur tortor ornare id. Vivamus et arcu nunc. Morbi viverra quam id libero rutrum elementum. Integer nibh eros, varius eu euismod ac, accumsan congue mauris. Integer eu mattis dui. Pellentesque volutpat vehicula ultrices."
a = []
character = ('t','o')
for i in string.split():
     if i.endswith(character) :
         a.append(i)
print(a)

numbersinwords = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten'}


def n2w(n):
     if n in numbersinwords:
         return numbersinwords[n]
     else:
         return numbersinwords[n - n % 10] + " " + numbersinwords[n % 10].lower()


newString = a

dictionary = {}
newString.sort(key=len)

for word in newString:
     dictionary[n2w(len(word))] = [word]
for word in newString:
     dictionary[n2w(len(word))].append(word)
for key in dictionary:
     dictionary[key].pop(0)

print("Dictionary: " + str(dictionary))
for key in dictionary:
     print("Sum of "+key+": "+str(len(dictionary[key])*len(dictionary[key][0])))


def pyramid(n):

    for i in range(1,n + 1):
        print((n - i) * ' ' + i * '* ')

pyramid(10)



def Hypotenuse():
    a=float(input("Input the lenght of the side a: "))
    b=float(input("Input the lenght of the side b: "))
    c = sqrt(a**2 + b**2)
    print("The hypotenuse lenght is: ", c)

Hypotenuse()

def fibonacci():
    f1, f2 = 0,1
    count = 0
    n = int(input("How many terms: "))
    if (n < 1):
        print("Must be positive")
        return
    else:
     while count < n:
        print(f1)
        sum = f1 + f2
        f1 = f2
        f2 = sum
        count +=1

fibonacci()