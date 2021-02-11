# 1. Напишете функция която приема 2 параметъра за катетите
# на правоъгълен триъгълник и изчислява хипотенузата му.
import math


def find_hypotenuse(a, b):
    powered = math.pow(a, 2) + math.pow(b, 2)
    c = math.sqrt(powered)
    print("For sides: a = %f and b = %f hypotenuse is: %f" % (a, b, c))


# --------------------------------------------------------
# 2. Напишете функция която приема 1 параметър за броя на
# редовете в следната фигура и я отпечатва на конзолата.

#         *
#       * * *
#     * * * * *
#   * * * * * * *


def print_pyramid(rows):
    white = ' '
    indent = '  '
    star = '*'
    reverse_rows = 1
    print("For rows = %d pyramid is:" % rows)
    while rows > 0:
        print(indent * rows + (star + white) * reverse_rows)
        reverse_rows += 2
        rows -= 1


# --------------------------------------------------------
# 3. Напишете функция която отпечатва първите N на брой
# елемента в редицата на Фибоначи.


def print_fibonacci(n, loop=0):
    if loop == 0:
        print("For n = %d fibonacci is:" % n)

    f0 = 0
    f1 = 1

    while loop < n:
        loop += 1
        if loop == 1:
            if loop == n:
                print("%d" % f0, end="")
                continue
            print("%d" % f0, end=", ")
            continue
        if loop == 2:
            if loop == n:
                print("%d" % f1, end="")
                continue
            print("%d" % f1, end=", ")
            continue

        next_num = f0 + f1
        f0 = f1
        f1 = next_num

        if loop != n:
            print("%d" % next_num, end=", ")
        if loop == n:
            print("%d" % next_num, end="")


print("Task 1: ")
find_hypotenuse(3, 4)
print("\nTask 2: ")
print_pyramid(5)
print("\nTask 3: ")
print_fibonacci(10)
