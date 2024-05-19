#  program to count the number of times a substring appears in the main string
import introJitendra
introJitendra.printIntro("program to count the number of times a substring appears in the main string")

mainString = input("enter main string : ")
substring = input("enter sub string : ")
occurrences = mainString.find(substring)
print(f"The substring '{substring}' appears at {occurrences} first in the main string.")
