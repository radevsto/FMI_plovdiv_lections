num_of_rows = int(input("Number of rows: "))


def print_stars(n):
    num_of_spaces = 2*n - 2
    num_of_stars = 1

    for i in range(0, n):
        for j in range(0, num_of_spaces):
            print(end=" ")

        num_of_spaces -= 2

        for k in range(0, num_of_stars):
            print("*", end=" ")

        num_of_stars += 2
        print()


print_stars(num_of_rows)
