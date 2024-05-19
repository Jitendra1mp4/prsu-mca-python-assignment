# Python program to demonstrate the use of lambda functions and reduce
import introJitendra
from functools import reduce
introJitendra.printIntro("program to demonstrate the use of lambda functions and reduce.")

nums = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)
print("Product of numbers:", product)
