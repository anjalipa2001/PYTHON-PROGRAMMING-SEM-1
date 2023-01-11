#Program to find the factorial of a number
''''n=int(input("Enter the number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial =",fact)'''
def calc_factorial(x):
    if x==1:
        return 1
    else:
        return(x*calc_factorial(x-1))
n=int(input("Enter the number:"))
print("Factorial =",calc_factorial(n))