from Graphics.rectangle import*
from Graphics.circle import*
from Graphics.threeDgraphics.cuboid import*
from Graphics.threeDgraphics.sphere import*

l=int(input("Enter the length of the rectangle : "))
b=int(input("Enter the bradth of the rectangle : "))
print("Area of Rectangle = ",RectArea(l,b))
print("Perimeter of rectangle = ",RectPerimeter(l,b))


r=int(input("Enter the radius of the circle : "))
print("Area of circle = ",CirArea(r))
print("Perimeter of circle = ",CirPerimeter(r))

l=int(input("Enter the length of the cuboid : "))
b=int(input("Enter the bradth of the cuboid : "))
h=int(input("Enter the height of the cuboid : "))
print("Area of cuboid  = ",CubArea(l,b,h))
print("Perimeter of cuboid  = ",CubPerimeter(l,b,h))

r=int(input("Enter the radius of the sphere : "))
print("Area of sphere = ",SphArea(r))
print("Perimeter of sphere = ",SphPerimeter(r))



