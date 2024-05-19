#  check whether a string entered by the user is a valid decimal number or not
import introJitendra
introJitendra.printIntro(" check whether a string entered by the user is a valid decimal number or not")

s = input("Enter a string: ")
isDecimal = True
for i in s : 
    if not((i >= '0' and i <= '9') or i=='.'):
        isDecimal = False

if isDecimal : print(s , " is decimal")
else : print(s , " is not a decimal")
