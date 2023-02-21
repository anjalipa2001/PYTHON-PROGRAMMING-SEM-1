'''num=int(input("Enter the Number :"))
n1,n2=0,1
print("Fibonacci series :",n1,n2,end=" ")
for i in range(2,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")
print()'''

def fibonacci(n):
    if n<=1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
n=int(input("Enter the number to find the fibonacci :"))
print("Fibonacci is :")
for i in range(n):
    print(fibonacci(i))
    
               