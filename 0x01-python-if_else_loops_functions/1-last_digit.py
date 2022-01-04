#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    l_dgt = ((number * -1) % 10) * -1
else:
    l_dgt = number % 10

if l_dgt > 5:
    print("Last string of {:d} is {:d} and is greater than 5".format(number, l_dgt))
elif l_dgt == 0:
    print("Last string of {:d} is 0".format(number))
else:
    print("Last string of {:d} is {:d} and is less than 6 and not 0".format(number, l_dgt))
