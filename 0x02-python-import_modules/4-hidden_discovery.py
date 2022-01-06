#!/usr/bin/python3.4
if __name__ == "__main__":
    from sys import path
    path.append('./')
import hidden_4
x = 8
mth = dir(hidden_4)
for X in range(1, 4):
    print("{}".format(mth[x]))
    x += 1
