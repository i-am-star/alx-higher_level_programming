#!/usr/bin/python3
import sys

num = len(sys.argv) - 1
argg = sys.argv
calc = 0

for i in range(num):
    calc = calc + int(argg[i + 1])
print("{}".format(calc))
