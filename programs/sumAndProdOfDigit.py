#Find the sum and product of digits of a number:
import introJitendra
introJitendra.printIntro("Find the sum and product of digits of a number:")

num = input("Enter a number: ")
sum_of_digits = 0
for i in num :
    sum_of_digits += int(i) 

product_of_digits = 1
for digit in num:
    product_of_digits *= int(digit)
print("Sum of digits: ", sum_of_digits)
print("Product of digits: ", product_of_digits)