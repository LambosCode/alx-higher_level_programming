#!/usr/bin/python3
def uniq_add(my_list=[]):
    y = len(my_list)
    x = 0
    z = 1
    while x < y and z < y:
        if my_list[x] != my_list[z]:
            z = z + 1
            if z == y:
                z = 0
                x = x + 1
                z = x + 1
        else:
            my_list.pop(z)
            y = len(my_list)
    z = 0
    for i in my_list:
        z = z + i
    return z
