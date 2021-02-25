import argparse


def main():
    parser = argparse.ArgumentParser(description="Name of files")
    parser.add_argument('--nargs', nargs='+')
    test_files = dict(parser.parse_args()._get_kwargs())["nargs"]

    for test_file in test_files:
        test_file_name = test_file + ".txt"
        # the path might be different on your computer
        f = open("C:/Users/User/Desktop/lection4-exercise/FMI_plovdiv_lections/longest_adjacent_sequence/jordan_kondakov/tests/" + test_file_name)
        file_content = f.readlines()

        size = file_content[0].replace("\n", "").split(" ")
        field = []

        count = 1
        while count <= int(size[0]):
            row = file_content[count].replace("\n", "").split(" ")
            field.append(row)
            count += 1

        visited = [[0 for j in range(int(size[0]))]
                   for i in range(int(size[0]))]
        result = [[0 for j in range(int(size[0]))]for i in range(int(size[0]))]
        COUNT = 0

        # checks if a cell is valid (it is inside the matrix and equal to the key)
        def is_valid(x, y, key, field):
            if (x < int(size[0]) and y < int(size[0]) and x >= 0 and y >= 0):
                if (visited[x][y] == 0 and field[x][y] == key):
                    return True
                else:
                    return False

            else:
                return False

        # BFS to find all cells that are connected to field[i][j]
        def BFS(x, y, i, j, field):
            global COUNT

            # terminating case for BFS
            if (x != y):
                return

            visited[i][j] = 1
            COUNT += 1

            # posible movements for x and y
            x_move = [0, 0, 1, -1]
            y_move = [1, -1, 0, 0]

            # checks if all four points are connected to field[i][j]
            for u in range(4):
                if (is_valid(i + y_move[u], j + x_move[u], x, field)):
                    BFS(x, y, i + y_move[u], j + x_move[u], field)

        def reset_visited():
            for i in range(int(size[0])):
                for j in range(int(size[0])):
                    visited[i][j] = 0

        # if a longer color sequence is found, store it
        def reset_result(key, field):
            for i in range(int(size[0])):
                for j in range(int(size[0])):
                    if (visited[i][j] != 0 and field[i][j] == key):
                        result[i][j] = visited[i][j]
                    else:
                        result[i][j] = 0

        def print_result(res):
            print("The longest color sequence for file '" +
                  test_file_name + "' is " + str(res))

            # prints the longest color sequence
            for i in range(int(size[0])):
                for j in range(int(size[0])):
                    if (result[i][j] != 0):
                        print("*", end=' ')

                    else:
                        print('- ', end='')

                print()

        def find_longest_sequence(field):
            global COUNT
            current_max = -10000000000

            for i in range(int(size[0])):
                for j in range(int(size[0])):
                    reset_visited()
                    COUNT = 0

                    # check the right cell
                    if (j + 1 < int(size[0])):
                        BFS(field[i][j], field[i][j + 1], i, j, field)

                    # updating the result
                    if (COUNT >= current_max):
                        current_max = COUNT
                        reset_result(field[i][j], field)

                    reset_visited()
                    COUNT = 0

                    # check the bottom cell
                    if (i + 1 < int(size[0])):
                        BFS(field[i][j], field[i + 1][j], i, j, field)

                    # updating the result
                    if (COUNT >= current_max):
                        current_max = COUNT
                        reset_result(field[i][j], field)

            print_result(current_max)

        find_longest_sequence(field)
        
        # test_4 won't work because it's not the right format
        # run python main.py --nargs *the names of the files you want to find the longest color sequence for seperated by ' '* (example: python main.py --nargs test_1 test_2)

        f.close()


if __name__ == "__main__":
    main()
