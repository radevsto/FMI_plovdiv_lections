# 1. Напишете функция която приема 2 параметъра за катетите на правоъгълен триъгълник и изчислява хипотенузата му.
import math


def find_hyp(a, b):
    powered = math.pow(a, 2) + math.pow(b, 2)
    c = math.sqrt(powered)
    print(f"The hypotenuse is {c} with {a} and {b} as the other sides of the triangle.")


print("Task 1:")
find_hyp(3, 4)


# 2. Напишете функция която приема 1 параметър за броя на редовете в следната фигура и я отпечатва на конзолата.
def print_pyramid(n):
    blank = ' '
    indent = '  '
    star = '*'
    rows = 1
    while n > 0:
        print(indent * n + (star + blank) * rows)
        rows += 2
        n -= 1


print("\nTask 2: ")
print_pyramid(6)


# 3. Напишете функция която отпечатва първите N на брой елемента в редицата на Фибоначи.
def fibonacci(n):
    if n < 0:
        return -1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_print(n):
    if n <= 0:
        print("Number should be positive.")
    else:
        for i in range(0, n):
            print(fibonacci(i))


print("\nTask 3: ")
fibonacci_print(7)
