from graphics.rectangle import*
from graphics.circle import*
from graphics.threeDgraphics.sphere import*
from graphics.threeDgraphics.cuboid import*

l=int(input("Enter the length of the rectangle :"))
b=int(input("Enter the breadth of the rectangle :"))
print("AREA OF THE RECTANGLE : ",rectarea(l,b))
print("PERIMETER OF THE RECTANGLE : ",rectperi(l,b))

r=int(input("Enter the radius :"))
print("AREA OF THE CIRCLE : ",circarea(r))
print("PERIMETER OF THE CIRCLE : ",circperi(r))

r=int(input("Enter the radius :"))
print("AREA OF THE SPHERE : ",spharea(r))
print("PERIMETER OF THE SPHERE : ",sphperi(r))

l=int(input("Enter the length of the cuboid :"))
b=int(input("Enter the breadth of the cuboid :"))
h=int(input("Enter the height of the cuboid :"))
print("AREA OF THE CUBOID : ",cubarea(l,b,h))
print("PERIMETER OF THE CUBOID : ",cubperi(l,b,h))







