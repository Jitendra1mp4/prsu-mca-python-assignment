#  check and print if entered string is palindrome or not
import introJitendra
introJitendra.printIntro("check and print if entered string is palindrom or not")

s=input("enter the string to be checked : ") ;
isPalindrome=True 
for i in range(len(s)//2):
    if s[i] != s[-(i+1)] :
        print("no palindrome")
        isPalindrome=False ;
        break ;
if isPalindrome : print("Palindrome")