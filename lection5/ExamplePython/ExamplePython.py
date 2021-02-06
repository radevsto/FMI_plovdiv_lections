import math

## Preparation Functions
def print_exercise_header(n: str, isEnd: bool):
    if(not isEnd):
        print(f"Start of Exercise {n}\n")   
    else:
        print(f"\nEnd of Exercise {n}\n")

## Exercises

print_exercise_header(1,False)

#1. Напишете функция която приема 2 параметъра за катетите
#на правоъгълен триъгълник и изчислява хипотенузата му.

# Solution
# -----------------------------------------------------------------------------------

def pythagoras_function_print(a: int, b:int):
       print(math.sqrt((a ** 2 + b ** 2)))

pythagoras_function_print(2,5)

# -----------------------------------------------------------------------------------

print_exercise_header(1,True)

#2. Напишете функция която приема 1 параметър за броя на
#редовете в следната фигура и я отпечатва на конзолата.

#*

#* * *

#* * * * *

#* * * * * * *

print_exercise_header(2,False)

# Solution
# -----------------------------------------------------------------------------------

def star_print(n: int):
    element = " * "
    spaces = " " * (n * 6)

    i = 1
    s = 1

    for x in range(1, n + 1):
        stars = spaces + (element * i)
        print(stars[(i + s)::])
        i += 2
        s += 1

star_print(8)

# -----------------------------------------------------------------------------------

print_exercise_header(2,True)

#3. Напишете функция която отпечатва първите N на брой
#елемента в редицата на Фибоначи.

print_exercise_header(3,False)

# Solution
# -----------------------------------------------------------------------------------

def fib_generator(n: int):
    if n < 0:
        return "Invalid Value"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_generator(n - 1) + fib_generator(n - 2)
   
def fib_print(n):
    if n <= 0:
        print("Invalid Value")
    else:
        for i in range(0, n):
            print(fib_generator(i))

fib_print(10)

# -----------------------------------------------------------------------------------

print_exercise_header(3,True)