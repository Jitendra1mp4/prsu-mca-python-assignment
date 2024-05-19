# Exception Handling Program that uses try, except and else
import introJitendra
introJitendra.printIntro("Exception Handling Program that uses try, except and else.")

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Division by zero occurred.")
else:
    print("Result:", result)

