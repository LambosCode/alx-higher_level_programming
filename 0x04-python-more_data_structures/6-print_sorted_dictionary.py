#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dixt = sorted(a_dictionary)
    for x in dixt:
        print("{}: {}".format(x, a_dictionary[x]))

