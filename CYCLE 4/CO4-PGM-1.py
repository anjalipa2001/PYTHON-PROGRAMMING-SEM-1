class rectangle:
    def __init__(self):
        self.length=int(input("Enter the length of the rectangle :"))
        self.breadth=int(input("Enter the breadth of the rectangle :"))
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def area(self):
        return self.length*self.breadth
    def compare(self,r2):
        if r1.area()>r2.area():
            print("Area of rectangle 1 is greater.")
        elif r2.area()>r1.area():
            print("Area of rectangle 2 is greater.")
print("Enter the length and the breadth of the first rectangle")
r1=rectangle()
print("Enter the length and the breadth of the second rectangle")
r2=rectangle()
print("Area of the first rectangle :",r1.area())
print("Area of the second rectangle :",r2.area())
print("Perimeter of the first rectangle :",r1.perimeter())
print("Perimeter of the second rectangle :",r1.perimeter())
r1.compare(r2)
