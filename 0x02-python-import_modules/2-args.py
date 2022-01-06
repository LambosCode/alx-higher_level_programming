#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
if len(argv) >= 3:
    print("{} arguments:".format(len(argv) - 1))
elif len(argv) == 1:
    print("{} argument.".format(len(argv) - 1))
else:
    print("{} argument:".format(len(argv) - 1))
for x in range(1, len(argv)):
    print("{}: {}".format(x, argv[x]))
