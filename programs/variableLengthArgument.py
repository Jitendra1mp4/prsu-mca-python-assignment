# Function to demonstrate variable length arguments
import introJitendra
introJitendra.printIntro("Python function to demonstrate variable length arguments.")

def variable_length_args(*args):
    print("Variable length arguments demo:")
    for arg in args:
        print(arg)

variable_length_args(1, 2, 3, 4, 5)
