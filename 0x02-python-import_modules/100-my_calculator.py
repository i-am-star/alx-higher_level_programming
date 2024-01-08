#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    num = len(sys.argv)

    if num != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a1 = sys.argv[1]
    op = sys.argv[2]
    b2 = sys.argv[3]
    a = int(a1)
    b = int(b2)

    if op not in ['+', '-', '/', '*']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if op == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif op == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    elif op == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
