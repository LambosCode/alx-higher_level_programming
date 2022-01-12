#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    lst = list(a_dictionary.keys())
    for x in range(len(lst)):
        if lst[x] == key:
            del a_dictionary[key]
    return a_dictionary
