def even_numbers():
    for i in range(1,101):
        if i % 2 == 0:
            print(i)

def string_play():
    string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis tempus suscipit. Mauris efficitur interdum turpis, vitae varius nunc fringilla non. Vestibulum malesuada fringilla tellus vel iaculis. In vehicula gravida fermentum. Vivamus ultrices lacinia pretium. Mauris orci lectus, lacinia at placerat ut, aliquam at quam. Donec condimentum feugiat arcu, ut consectetur tortor ornare id. Vivamus et arcu nunc. Morbi viverra quam id libero rutrum elementum. Integer nibh eros, varius eu euismod ac, accumsan congue mauris. Integer eu mattis dui. Pellentesque volutpat vehicula ultrices."
    string = string.replace('.','')
    string = string.replace(',', '')
    array = string.split(' ')
    return(array)

def word_play():

    array = string_play()
    for i in array:
        if i[-1:] == 'o':
            print(i)
        elif i[-1:] == 't':
            print(i)

def dicty():
    array = string_play()
    sorted_array = sorted(array, key=len)
    dictionary = {}
    spelled = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6:"six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve"}
    for word in sorted_array:
        dictionary.setdefault(len(word), []).append(word)
    count = 0
    for key in dictionary.keys():
        j=0
        for elem in dictionary[key]:
            j+=1
        count = count + (j * int(key))
    for key in dictionary.keys():
        print(spelled[key] + " - " + str(dictionary[key]))
    print("Number of letters in the string: " + str(count))


class MyTriangle(object):

    def __init__(self, base=0, height=0):  # 0 for b & h if nothing is passed in
        self.base = base
        self.height = height

    def setBase(self, base):
        self.base = base

    def getBase(self):
        return self.base

    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height

    def getHypoth(self):
        hypoth = (self.height ** 2 + self.base ** 2) // 2
        return hypoth

def hypotenuse(a, b):

    print(a,b)
    t1 = MyTriangle(a, b)
    print(t1.getHypoth())

def isosceles(a):
    i = 1
    y = i
    p = a
    for i in range(a):
        print(p*" " + y*"*" + p*" ")
        y=y+2
        p=p-1

def fibonacchi(a):
    i = y = 0
    x = 1
    if a > 0:
        for i in range(a):
            z = y + x
            print(z)
            x = y
            y = z
    else:
        print("Unexpected lenght")


def main():

    import sys
    print("Task number: ")
    option = raw_input(" 1 - Event Numbers in 1:100 \n "
                       "2 - Words ending in \'o\' and \'t\' \n "
                       "3 - Dictionary ops: \n "
                       "4 - Hypotenuse of triangle: \n "
                       "5 - Draw an isosceles triangular: \n "
                       "6 - First N elements of Fibonacci Numbers: \n ")
    print("Selection option is " + option)

    if option == '1':
        even_numbers()
    elif option == '2':
        word_play()
    elif option == '3':
        dicty()
    elif option == '4':
        a = int(raw_input("Enter base: \n"))
        b = int(raw_input("Enter hight: \n"))
        hypotenuse(a, b)
    elif option == '5':
        a = int(raw_input("Enter rolls: \n"))
        isosceles(a)
    elif option == '6':
        a = int(raw_input("Enter rolls: \n"))
        fibonacchi(a)
    else:
        print ("Unknown selection")
        sys.exit(1)
if __name__ == '__main__':
    main()