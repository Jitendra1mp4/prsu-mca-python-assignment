# Program to demonstrate default arguments of a function
import introJitendra
introJitendra.printIntro("Python program to demonstrate the default arguments of a function.")

def default_demo(x=1, y=1):
    print("Default arguments demo:")
    print("x:", x)
    print("y:", y)

default_demo()
default_demo(3)
default_demo(3, 5)
