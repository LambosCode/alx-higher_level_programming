#!/usr/bin/python3
def islower(c):
    cnt = 0
    while c[cnt] != 0:
        for i in range(97, 123):
            if c[cnt] == chr(i):
                return True
            else:
                return False
        cnt += 1
