def output(number):
    for i in range(number):
        print(' ' * (number - (i + 1)), '*' * (2 * i + 1))


print("Count rows: ")
number = int(input())

output(number);
