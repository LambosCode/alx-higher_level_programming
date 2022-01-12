#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    cnt = len(matrix)
    matrix1 = []
    x = 0
    cnt_1 = lambda x: x+1
    for i in range(cnt):
        matrix1.append(list(map(lambda x: x*x, matrix[x])))
        x = cnt_1(x)
    return matrix1
