character = '*'


def draw_n_row_figure(num_rows):
    if num_rows <= 0:
        raise Exception("Number of rows should be positive number.")
    for row in range(num_rows):
        count = 0
        for i in range(0, num_rows - row - 1):
            print(" ", end="")
        for j in range(row + 1):
            print("*", end="")
            if count < row:
                print("*", end="")
                count += 1
        print()
