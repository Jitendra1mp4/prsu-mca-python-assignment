# Access each element of a string in forward and backward orders using the 'for' loop:
import introJitendra
introJitendra.printIntro("Access each element of a string in forward and backward orders using the 'for' loop:")
def access_string(s):
    for char in s:
        print(char,end='')

    print('')
    for char in reversed(s):
        print(char,end='')

str1 = input("enter a string ")
access_string(str1)