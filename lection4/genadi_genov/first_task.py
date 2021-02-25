def is_even_number(number):
    return number % 2 == 0


def print_even_numbers():
    print("-----\nEven numbers in range 1 to 100 inclusive:\n-----")
    for number in range(1, 101, 1):
        if is_even_number(number):
            print(number)
    print("-----\nEND\n-----")
