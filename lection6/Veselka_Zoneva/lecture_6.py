import math


# 1 - pythagorean theorem
def pt(a, b):
    return math.sqrt(pow(a, 2) + pow(b, 2))


print("{:.2f}".format(pt(5, 6)))
print("{:.2f}".format(pt(3, 4)))
print()


# 2 - 2d pyramid figure
def pyramid(n):
    for i in range(1, n + 1):
        for f in range(1, (n - i) + 1):
            print(end="  ")

        for j in range(0, (i * 2) - 1):
            print(end='* ')
        print()


pyramid(5)
print()


# 3 - fibonacci
def fibonacci_fact(n):
    count = 2
    numbers = [0, 1]

    def fibonacci(j):
        nonlocal count
        while count < j:
            numbers.append(numbers[len(numbers) - 1] + numbers[len(numbers) - 2])
            count += 1

    fibonacci(n)
    return numbers


print(fibonacci_fact(10))
