#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, modules
modules['3-infinite_add'] = None
y = 0
for x in range(1, len(argv)):
    y = y + int(argv[x])
print("{}".format(y))
