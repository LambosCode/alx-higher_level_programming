#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    ln = len(my_list)
    while not ln < 1:
        ln = ln - 1
        print("{:d}".format(my_list[ln]))
