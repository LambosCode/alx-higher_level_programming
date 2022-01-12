#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list1 = my_list.copy()
    x = lambda x:x+1
    z = 0
    for cnt in range(len(my_list1)):
        if my_list1[z] == search:
            my_list1[z] = replace
        z = x(z)
    return my_list1
