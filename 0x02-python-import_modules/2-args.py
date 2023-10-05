#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_arg = len(sys.argv) - 1
    if num_arg == 0:
        print("0 argument.")
        elif num_arg == 1:
            print("1 argument:")
        else:
            print("{} argument:".format(num_arg))
            for index in range(num_arg):
                print("{}: {}".format(index + 1, sys.argv[index + 1]))
