# Access each element of a string in forward and backward orders using the 'while' loop:
import introJitendra
introJitendra.printIntro("Access each element of a string in forward and backward orders using the 'while' loop:")
def access_string(s):
    i = 0
    while i < len(s):
        print(s[i],end='')
        i += 1
    
    i = len(s) - 1
    print('')
    while i >= 0:
        print(s[i],end='')
        i -= 1

str1 = input("enter a string ")
access_string(str1)
