# Python program to print the CWD and change the CWD
import introJitendra
import os
introJitendra.printIntro("Write a Python program to print the CWD and change the CWD.")

print("Current working directory:", os.getcwd())
new_dir = input("Enter the path for the new directory: ")
os.chdir(new_dir)
print("Changed working directory to:", os.getcwd())

