# program to implement function to greet user
# 23/01/23
def greeting(name):
    print("Hello " + name + "!")


def birthday(age):
    print("Congratulations on turning " + str(age) + "!")


greeting(input("What is your name? "))
birthday(input("What age did you just turn? "))
