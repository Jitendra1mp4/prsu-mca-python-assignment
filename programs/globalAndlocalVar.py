# Program to demonstrate global and local variables
import introJitendra
introJitendra.printIntro("demonstrate global and local variables.")

global_var = "I am a global variable"

def local_demo():
    local_var = "I am a local variable"
    print("Inside the function:", local_var)
    print("Inside the function accessing global variable:", global_var)

local_demo()
print("Outside the function accessing global variable:", global_var)

