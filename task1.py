from math import sqrt

def hypotenuse(a, b):
    print("Input lengths of shorter triangle sides:")
    c = sqrt(a**2 + b**2)
    print("The length of the hypotenuse is", c )

hypotenuse(5,5)
