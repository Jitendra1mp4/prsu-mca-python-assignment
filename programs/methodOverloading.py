# Python program to demonstrate “Method Overloading”
import introJitendra

introJitendra.printIntro("Write a Python program to demonstrate “Method Overloading”.")

class Adder:
    def total(self, a=None, b=None, c=None):
        if c != None:
            return a + b + c
        if b != None:
            return a + b
        if a != None:
            return a


# Create an instance of the class
obj = Adder()

# Call the sum method with different numbers of arguments
print("enter two numbers : ")
x = int(input())
y = int(input())
print(f"Sum of {x} and {y} = {obj.total(x, y)}")

print("enter three numbers : ")
x = int(input())
y = int(input())
z = int(input())
print(f"Sum of {x}, {y} and {z}= {obj.total(x, y, z)}")
