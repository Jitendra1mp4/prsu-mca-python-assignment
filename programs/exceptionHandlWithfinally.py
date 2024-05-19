# Exception Handling Program that uses finally with try
import introJitendra
introJitendra.printIntro("Exception Handling Program that uses finally with try.")

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Division by zero occurred.")
finally:
    print("This will always execute, regardless of an exception.")
