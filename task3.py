def fib(n):
    f1 = 0
    f2 = 1
    if (n < 1):
        return
    for x in range(0, n):
        print(f2, end=" ")
        next = f1 + f2
        f1 = f2
        f2 = next

fib(8)
