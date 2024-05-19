# Exception Handling Program that uses try and except
import introJitendra
introJitendra.printIntro("Exception Handling Program that uses try and except.")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred.")
