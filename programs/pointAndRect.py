# Python program that creates classes “Point” and “Rectangle” where the Rectangle class has a Point object as its attribute
import introJitendra

introJitendra.printIntro("Write a Python program that creates classes “Point” and “Rectangle” where the Rectangle class has a Point object as its attribute.")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        return (self.x == other.x) and (self.y == other.y)

    def printPoint(self):
        print("x = ", self.x)
        print("y = ", self.y)


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def print(self):
        self.point1.printPoint()
        self.point2.printPoint()


x = float(input("enter x for point 1 : "))
y = float(input("enter y for point 1 : "))
p1 = Point(x, y)
x = float(input("enter x for point 2 : "))
y = float(input("enter y for point 2 : "))
p2 = Point(x, y)

if (not(p1==p2)):
    rect1 = Rectangle(p1,p2)
    print("created rectangle!\nPrinting points...")
    rect1.print()
else : print("both point should not be same")
