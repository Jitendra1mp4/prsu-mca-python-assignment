#  check if a year entered by the user is a Leap Year or NOT
import introJitendra
introJitendra.printIntro(" check if a year entered by the user is a Leap Year or NOT")

year = int(input("Enter a year: "))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(year," is a leap year")
        else:
            print(year," is not a leap year")
    else:
        print(year," is a leap year")
else:
    print(year," is not a leap year")
