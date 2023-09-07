#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1
    if argc == 0:
        print("Number of argument(s): .")
    elif argc == 1:
        print("Number of argument(s): 1 argument")
        print("1: {}".format(sys.argv[1]))
    else:
        print("Number of argument(s): {} arguments".format(argc))
        for i in range(argc):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
