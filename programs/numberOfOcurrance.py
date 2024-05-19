# Python program to find the number of occurrences of each letter in a string using dictionaries
import introJitendra
introJitendra.printIntro("Write a Python program to find the number of occurrences of each letter in a string using dictionaries.")

string = input("Enter a string: ")
letter_count = {}
for char in string:
    if char in letter_count:
        letter_count[char] += 1
    else:
        letter_count[char] = 1

print("Occurrences of each letter:")
for char, count in letter_count.items():
    print(char, ":", count)

