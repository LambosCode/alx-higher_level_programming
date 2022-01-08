#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
mth = dir()
for x in range(1, len(mth)):
    if mth[x][0] == '_' and mth[x][1] == '_':
        continue
    else:
        print("{}".format(mth[x]))
