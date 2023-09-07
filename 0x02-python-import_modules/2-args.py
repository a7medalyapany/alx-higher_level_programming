#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("Number of argument(s): .")
    elif count == 1:
        print("Number of argument(s): 1 argument")
        print("1: {}".format(sys.argv[1]))
    else:
        print("Number of argument(s): {} arguments".format(count))
        for i in range(count):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
