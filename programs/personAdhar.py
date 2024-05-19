# Python program that creates a class “Person”, with attributes [aadhar, name, DoB]
import introJitendra
introJitendra.printIntro("Write a Python program that creates a class “Person”, with attributes [aadhar, name, DoB].")

class Person:
    def __init__(self, aadhar, name, dob):
        self.aadhar = aadhar
        self.name = name
        self.dob = dob
    
    def print(self):
        print(f"name :{self.name}\ndob : {self.dob}\naadhar : {self.aadhar}\n")

name=input("enter name : ")
dob=input("enter dob : ")
aadhar=input("enter aadhar : ")

p1 = Person(name=name,dob=dob,aadhar=aadhar)

print("\nPrinting details")
p1.print()
