# Fibonacci series up to N terms:
import introJitendra
introJitendra.printIntro("Fibonacci series up to N terms:")

def fibonacci(n):
    a, b = -1, 1
    while n > 0:
        a, b = b, a + b
        print(b, " ", end="")
        n -= 1

n = int(input('enter length of fibonacci series: '))
fibonacci(n)
