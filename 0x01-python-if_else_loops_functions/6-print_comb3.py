#!/usr/bin/python3
for i in range(0, 89):
    f_dgt = int(i / 10)
    l_dgt = i % 10
    if f_dgt >= l_dgt:
        continue
    else:
        print("{:d}{:d}".format(f_dgt, l_dgt), end=", ")
i += 1
print("{:d}".format(i))
