def fibonacci_number(number):
    if number <= 1:
        return number
    else:
        return fibonacci_number(number - 1) + fibonacci_number(number - 2)


def print_fibonacci_sequence(number_of_terms):
    if number_of_terms <= 0:
        raise Exception("Number of terms should be positive numbers.")
    else:
        print("Fibonacci sequence till term #" + str(number_of_terms))
        for i in range(number_of_terms):
            print(fibonacci_number(i))
