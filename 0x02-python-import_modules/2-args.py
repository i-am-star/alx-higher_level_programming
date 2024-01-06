#!/usr/bin/python3
import sys
num = len(sys.argv) - 1
argg = sys.argv

if num == 0:
    print("0 arguments.")
elif num == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(num))
for i in range(num):
    print("{}: {}".format(i + 1, argg[i + 1]))


# if __name__ == "__main__":
#    """Print the number of and list of arguments."""
#    import sys
#
#    count = len(sys.argv) - 1
#    if count == 0:
#        print("0 arguments.")
#    elif count == 1:
#        print("1 argument:")
#    else:
#        print("{} arguments:".format(count))
#    for i in range(count):
#        print("{}: {}".format(i + 1, sys.argv[i + 1]))
