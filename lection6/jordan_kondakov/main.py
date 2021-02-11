import math


def find_hypotenuse(a, b):
    print("The hypotenuse of a triangle with sides %s, %s is " %
          (a, b), math.hypot(a, b))


def get_triangle(n):
    spaces = n - 1
    for rows in range(0, n):
        for _ in range(0, spaces):
            print(end=" ")

        spaces -= 1
        for _ in range(0, rows + 1):
            print("* ", end="")

        print("\r")


def print_fibonacci_numbers(n):
    fibs = [0, 1]

    for _ in range(2, n + 1):
        fibs.append(fibs[-1] + fibs[-2])

    for number in fibs:
        print(number)


def main():
    # Exercise 1: Given two parameters, find the hypotenuse of a right-angled triangle
    find_hypotenuse(3, 4)

    # Exercise 2: Given the number of rows, print a triangle which consists of *
    # get_triangle(5)

    # Exercise 3: Given the number count, print Fibonacci numbers
    # print_fibonacci_numbers(40)


if __name__ == "__main__":
    main()
