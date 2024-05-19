# Function to take two integers as input and return their sum and product
import introJitendra
introJitendra.printIntro("function takes two integers and return their sum and product.")

def sum_and_product(a, b):
    return a + b, a * b

x=int(input("enter num1 : ")) ;
y=int(input("enter num2 : ")) ;

sum , prod = sum_and_product(x,y) 
print("sum : " , sum) 
print("product " , prod) 