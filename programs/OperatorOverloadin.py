# Python program to demonstrate “Operator Overloading” [+ and -] using a class “Book”
import introJitendra
introJitendra.printIntro("Write a Python program to demonstrate\n“Operator Overloading” [+ and -] using a class “Book”.")

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

    def __sub__(self, other):
        return self.pages - other.pages

book1 = Book(int(input("enter of pages in book 1 ")))
book2 = Book(int(input("enter of pages in book 2 ")))
print("Total pages after addition:", book1 + book2)
print("Difference in pages after subtraction:", book2 - book1)
