user_input = int(input("Enter a number: "))


def calculate_fibonacci(n):
    if n <= 1:
        return n
    return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)


if user_input <= 0:
    print("Invalid input!")
else:
    print(f"Fibonacci sequence for {user_input} elements:", end=" ")
    for i in range(user_input):
        print(calculate_fibonacci(i), end=" ")
