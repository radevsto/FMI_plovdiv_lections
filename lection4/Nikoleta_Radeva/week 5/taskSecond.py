def create_figure(x):
    n = 0
    for i in range(1, x + 1):
        for f in range(1, (x - i) + 1):
            print(end="  ")
        while n != (2 * i - 1):
            print("* ", end="")
            n = n + 1
        n = 0
        print()
create_figure(4)
