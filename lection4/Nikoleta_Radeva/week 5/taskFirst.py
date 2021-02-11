import math
def calcilate_hypotenuse():
    a = float(input('Please enter the side a: '))
    b = float(input('Please enter the side b: '))
    c = math.sqrt((a * a) + (b * b))
    print("The hypotenuse side is: ", c)
calcilate_hypotenuse()

