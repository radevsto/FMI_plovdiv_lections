import math


# task1

def find_hypotenuse(num1, num2):
    hypotenuse = math.sqrt(num1 ** 2 + num2 ** 2)
    return hypotenuse


# print(find_hypotenuse(3,4))

# task 2
def printTriangle(rows):
    for i in range(0, rows):
        print((rows - i) * ' ' + (i * 2 + 1) * '*' + (rows - i) * ' ')


# printTriangle(7)

# task 3
def fibonacci(num):
    n1 = 0
    n2 = 1
    sum = 0
    print(n1)
    print(n2)
    if (num >= 2):
        for i in range(2, num + 1):
            sum = n2 + n1
            n1 = n2
            n2 = sum
            print(sum)


#fibonacci(10)
