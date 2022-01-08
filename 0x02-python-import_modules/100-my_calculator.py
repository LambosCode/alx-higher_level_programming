#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
if len(argv) > 4 or len(argv) < 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
x = int(argv[1])
y = int(argv[3])
if argv[2] == "+":
    print("{:d} + {:d} = {:d}".format(x, y, add(x, y)))
elif argv[2] == "-":
    print("{:d} - {:d} = {:d}".format(x, y, sub(x, y)))
elif argv[2] == "*":
    print("{:d} * {:d} = {:d}".format(x, y, mul(x, y)))
elif argv[2] == "/":
    print("{:d} / {:d} = {:d}".format(x, y, div(x, y)))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
