#Find the sum and product of digits of a number:
import introJitendra
introJitendra.printIntro("GCD and LCM")

def getGCD(a,b):
    while(b!=0):
        temp = a 
        a = b 
        b = temp % b 
    return a 

def getLCM(a,b):
    max = a if a>b else b
    while True :
        if(max%a==0) and (max%b==0): break
        max+=1
    return max ;

x=int(input("enter namber 1 : "))
y=int(input("enter namber 2 : "))
print("x : ",x) 
print("y : ",y) 
print("GCD : ",getGCD(x,y))
print("LCM : ",getLCM(x,y))