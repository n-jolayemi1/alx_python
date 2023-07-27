#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    length = len(argv) - 1
    if length == 1:
        print("{} argument:".format(length))
    elif length == 0:
        print("{} arguments.".format(length))
    else:
        print("{} arguments:".format(length))

    for i in range(length+1):
        if i == 0:
            continue
        else:
            print("{}: {}".format(i, argv[i]))
