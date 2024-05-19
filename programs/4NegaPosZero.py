#  check if a number is Positive, Negative or Zero
import introJitendra
introJitendra.printIntro(" check if a number is Positive, Negative or Zero")

num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
