# Python program to demonstrate “Method Overriding”
import introJitendra
introJitendra.printIntro("Write a Python program to demonstrate “Method Overriding”.")

class Parent:
    def show(self):
        print("Parent's show method")

class Child(Parent):
    def show(self):
        print("Child's show method")

obj = Child()
obj.show()
