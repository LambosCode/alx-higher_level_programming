#!/usr/bin/python3
def add_tuple(tuple_a=(),tuple_b=()):
    summ = list()
    for x, i in zip(tuple_a, tuple_b):
            summ.append(x + i)
    tup = tuple(summ)
    return tup
