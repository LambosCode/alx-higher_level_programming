#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    ln = 0
    lnn = 0

    while ln < len(matrix):
        for x in matrix[ln]:
            print("{:d}".format(x), end='')
            if lnn < (len(matrix[ln]) - 1):
                print(" ".format(), end='')
            lnn = lnn + 1
        ln = ln + 1
        lnn = 0
        print("".format())
