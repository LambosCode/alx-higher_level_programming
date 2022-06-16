#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    summ = list()
    cnt = 0
    while cnt < 2:
        if type(tuple_a) is int or type(tuple_b) is int:
            summ.append(tuple_a + tuple_b)
            cnt += 1
            continue
        if cnt >= len(tuple_a):
            summ.append(tuple_b[cnt])
            cnt += 1
        elif cnt >= len(tuple_b):
            summ.append(tuple_a[cnt])
            cnt += 1
        else:
            summ.append(tuple_a[cnt] + tuple_b[cnt])
            cnt += 1
    sumd = tuple(summ)
    return sumd
