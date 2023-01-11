def add(a,b):
    '''adding two numbers a and b''' 
    add=a+b
    return add
#print("Addition",add)
def sub(a,b):
    sub=a-b
    return sub
#print("Substraction",sub)
def mul(a,b):
    mul=a*b
    return mul
#print("Multiplication",mul)
def div(a,b):
    div=a/b
    return div
#print("Division",div)
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c=int(input("Choose \n 1.Addition \n 2.Substraction\n 3.Multiplication \n 4.Division"))
if c==1:
    print(add(a,b))
elif c==2:
    print(sub(a,b))
elif c==3:
    print(mul(a,b))
elif c==4:
    print(div(a,b))

  