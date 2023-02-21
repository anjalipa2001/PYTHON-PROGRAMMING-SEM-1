class Publisher:
    def __init__(self,name):
        self.name=name 
    def display(self):
        print("Name of the publisher is :",self.name)
class Book(Publisher):
    def __init__(self,name,title,author):
        Publisher. __init__(self,name)
        self.title=title
        self.author=author
    def display(self):
        print("Title of the book is:",self.title)
        print("Author of the book is :",self.author)
class Python(Book):
    def __init__(self,name,title,author,price,no_of_pages):
        Book. __init__(self,name,title,author)
        self.price=price
        self.no_of_pages=no_of_pages
    def display(self):
        Publisher.display(self)
        Book.display(self)
        print("Price of the book is : ",self.price)
        print("No of pages is : ", self.no_of_pages)
p1=Python("Pearsons",'Object Oriented Modeling and Design',"Dr.Craig Larman",'$400',600)
p1.display()
