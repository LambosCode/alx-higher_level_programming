#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list1 = my_list.copy()
    y = lambda x: x+1
    i, j, result = 1, 0, 0
    cnt = len(my_list1)
    for x in range(0, cnt):
        if i < cnt - 1:
            if my_list1[j] == my_list1[i]:
                my_list1.pop(i)
            i = y(i)
            if i >= len(my_list1):
                j = y(j)
                i = 0
    cntd = len(my_list1)
    for x in range(cntd):
        result = result + my_list1[x]
    return result
