# Function to demonstrate keyword variable length arguments
import introJitendra
introJitendra.printIntro("Python function to demonstrate keyword variable length arguments.")

def keyword_variable_length_args(**kwargs):
    print("Keyword variable length arguments demo:")
    for key, value in kwargs.items():
        print(key, ":", value)

keyword_variable_length_args(name="Jitendra", age=30, city="Jitendra")
