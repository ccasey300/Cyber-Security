# program to take two parameters, perform exponent operations
# 27/01/23
def powers_for(num3, num4):
    result = 1
    for index in range(num4):
        result = result * num3
    return result


num = 2
numx = 3

print(powers_for(num, numx))

