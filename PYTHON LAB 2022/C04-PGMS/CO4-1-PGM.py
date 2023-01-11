class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def get_perimeter(self):
        return 2*(self.l + self.b)
    def get_area(self):
        return self.l*self.b
    def compare(self,s):
        try:
            if r.get_area()==s.get_area():
                print("Both area are equal")
            elif r.get_area()>s.get_area():
                print("largest area is :",r.get_area())
            else:
                print("largest area is :",s.get_area())
        except:
            print("No exception")
l1=int(input("Enter the length of the rectangle l1 :"))
b1=int(input("Enter the breadth of the rectangle b1 :"))
l2=int(input("Enter the length of the rectangle l2 :"))
b2=int(input("Enter the breadth of the rectangle b2 :"))
r=rectangle(l1,b1)
s=rectangle(l2,b2)
print("Area of rectangle :",r.get_area())
print("Perimeter of rectangle :",r.get_perimeter())
print("Area of rectangle :",s.get_area())
print("Perimeter of rectangle :",s.get_perimeter())
r.compare(s)




    