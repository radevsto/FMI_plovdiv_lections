from math import sqrt, pow


def calculate_hypotenuse(first_cathetus, second_cathetus):
    return sqrt(pow(first_cathetus, 2) + pow(second_cathetus, 2))


def print_hypotenuse(first_cathetus, second_cathetus):
    if first_cathetus <= 0 or second_cathetus <= 0:
        raise Exception("First and second cathetus should be positive numbers.")
    print(
        "First cathetus: " + str(first_cathetus) + ", second cathetus: " + str(second_cathetus) + " - hypotenuse: " +
        str(calculate_hypotenuse(first_cathetus, second_cathetus)))
