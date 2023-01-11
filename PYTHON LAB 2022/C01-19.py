'''import math
x=int(input("Enter the value of x :"))
y=int(input("Enter the value of y :"))
a=math.gcd(x,y)
print("The gcd of x and y is :",a)'''
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)  
a=int(input("Enter the value of x :"))
b=int(input("Enter the value of y :"))
GCD=gcd(a,b)
print("GCD is:")
print(GCD)
        
