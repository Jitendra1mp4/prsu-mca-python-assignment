# Python program to demonstrate the use of lambda functions and map
import introJitendra
introJitendra.printIntro("program to demonstrate the use of lambda functions and map.")

nums = [1, 2, 3, 4, 5]
squared_nums = list(map(lambda x: x**2, nums))
print("Squared numbers:", squared_nums)
