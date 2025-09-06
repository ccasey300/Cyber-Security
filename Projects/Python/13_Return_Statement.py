# program to return values from functions
# 23/01/23
from math import*


def cube(num):
    return num*num*num


def square(num):
    return num*num


def root(num):
    return sqrt(num)


number = int(input("Enter a number: "))
result = number
operation = input("Choose operation, (s = square, c = cube, sqrt = square root)")
if operation == "s":
    result = square(number)
    print("The square of " + str(number) + " = " + str(result))
elif operation == "c":
    result = cube(number)
    print("The cube of " + str(number) + " = " + str(result))
elif operation == "sqrt":
    result = root(number)
    print("The square root of " + str(number) + " = " + str(result))
else:
    print()
