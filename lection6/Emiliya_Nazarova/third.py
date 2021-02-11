def fibonacci(number):
    n1 = 0
    n2 = 1
    count = 0

    while count < number:
        print(n1)
        newNumber = n1 + n2
        n1 = n2
        n2 = newNumber
        count += 1


number = int(input("Count numbers for Fibonacci sequence: "))
fibonacci(number)
