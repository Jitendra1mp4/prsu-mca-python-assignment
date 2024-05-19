#Find sum of natural numbers, up to N:
import introJitendra
introJitendra.printIntro("Find sum of natural numbers, up to N:")


N = int(input("Enter a number: "))
sum = (N * (N + 1)) // 2
print("Sum of natural numbers up to N: ", sum)