import math

first_side = int(input("Enter a: "))
second_side = int(input("Enter b: "))


def calculate_hypotenuse(a, b):
    return math.sqrt(pow(a, 2) + pow(b, 2))


result = calculate_hypotenuse(first_side, second_side)
print(f"The hypotenuse is: {round(result, 2)}")
