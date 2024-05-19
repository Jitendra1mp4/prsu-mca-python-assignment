# Exception Handling Program that handles multiple types of exceptions
import introJitendra
introJitendra.printIntro("Exception Handling Program that handles multiple types of exceptions.")

try:
    result = 10 / 'a'
except ZeroDivisionError:
    print("Error: Division by zero occurred.")
except TypeError:
    print("Error: Unsupported operation. Type mismatch.")
