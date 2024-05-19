# Program to demonstrate keyword arguments of a function
import introJitendra
introJitendra.printIntro("Python program to demonstrate the keyword arguments of a function.")

def keyword_demo(x, y):
    print("Keyword arguments demo:")
    print("x:", x)
    print("y:", y)

keyword_demo(y=5, x=3)
