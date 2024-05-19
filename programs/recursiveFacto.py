# Python function that takes an integer as input and calculates its factorial using recursion
import introJitendra
introJitendra.printIntro("calculates factorial using recursion.")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter an integer to calculate its factorial: "))
print("Factorial of", num, "is", factorial(num))

