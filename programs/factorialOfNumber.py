# factorial of a number
import introJitendra
introJitendra.printIntro("factorial of a number")

num = int(input("enter the number : "))
t = num
fact = 1
while num >= 1:
    fact *= num
    num -= 1
print("factorial of : ", t, " is : ", fact)
