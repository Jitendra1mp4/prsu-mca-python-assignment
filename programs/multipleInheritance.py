# Python program to demonstrate “Multiple Inheritance”
import introJitendra
introJitendra.printIntro("Write a Python program to demonstrate “Multiple Inheritance”.")

class A:
    def show_parent1(self):
        print("Parent Father")

class B:
    def show_parent2(self):
        print("Parent Mother")

class C(A, B):
    def show_child(self):
        print("Am child\n")

obj = C()
obj.show_parent1()
obj.show_parent2()
obj.show_child() 
