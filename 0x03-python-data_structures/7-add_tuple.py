#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    summ = list()
    cnt = 0
    while cnt < 2:
        if cnt >= len(tuple_a):
            summ.append(tuple_b[cnt])
            cnt += 1
        elif cnt >= len(tuple_b):
            summ.append(tuple_a[cnt])
            cnt += 1
        else:
            if tuple_a is None or tuple_b is None:
                summ.append(0)
                cmt += 1
            else:
                summ.append(tuple_a[cnt] + tuple_b[cnt])
                cnt += 1
    sumd = tuple(summ)
    return sumd
