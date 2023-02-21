class rectangle:
    def __init__(self):
        self.__length=int(input("Enter the length of the rectangle :"))
        self.__breadth=int(input("Enter the breadth of the rectangle :"))
    def __lt__(self,rect2):
        area1=self.__length*self.__breadth
        area2=rect2.__length*rect2.__breadth
        print("Area of rectangle 1 :",area1)
        print("Area of rectangle 2 :",area2)
        return area1<area2

print("Enter the length and the breadth of the rectangle 1")
rect1=rectangle()
print("Enter the length and the breadth of the rectangle 2")
rect2=rectangle()
if rect1<rect2:
    print("Rectangle 1 is less than rectangle 2")
elif rect2<rect1:
    print("Rectangle 1 is greater than rectangle 2")

