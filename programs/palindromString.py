#  check and print if entered string is palindrome or not
import introJitendra
introJitendra.printIntro("check and print if entered string is palindrom or not")
s=input("enter the string to be checked : ") ;
isPalindrome= s==s[::-1]
if isPalindrome : print("Palindrome")
else :   print("Not palindrome")
