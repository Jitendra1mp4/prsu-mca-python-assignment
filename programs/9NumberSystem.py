#Convert a Decimal number into Binary, Octal and Hexadecimal:
import introJitendra
introJitendra.printIntro("Convert a Decimal number into Binary, Octal and Hexadecimal")

def convert(num,base) :
    bn = ''
    while(num>0):
        dig = num % base
        if(dig<10):
            bn = bn + str(dig) 
        else :
            alpha = chr(65 + dig%10)
            bn = bn + alpha
        num //= base
    # printing the number    
    for i in range(len(bn)-1,-1,-1):
        print (bn[i],end='') ;
    print('')

num = int(input("Enter number to be converted : "))
print("Binary : ",end='')
convert(num=num,base=2)
print("Octal : ",end='')
convert(num=num,base=8)
print("Hexadecimal : ",end='')
convert(num=num,base=16)