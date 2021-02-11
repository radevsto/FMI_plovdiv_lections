def hypotenuse(a, b):
    if a <= 0 or b <= 0:
        return "Error"
    return (a ** 2 + b ** 2) ** 0.5


def star_pyramid(rows):
    spaces = rows - 1
    stars = 1
    for x in range(rows):
        print(" " * spaces, "x" * stars)
        spaces -= 1
        stars += 2


def fibonacci(n):
    list = [0, 1]
    if n == 0: return "Wrong value"
    if n == 1: return 0

    for x in range(n - 2):
        list.append(list[-1] + list[-2])
    return print(list)


print(hypotenuse(4, 3))
star_pyramid(4)
(fibonacci(7))
