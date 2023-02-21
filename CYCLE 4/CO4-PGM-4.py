class time:
    def __init__(self):
        self.__h=int(input("Enter the time in hours :"))
        self.__m=int(input("Enter the time in minutes :"))
        self.__s=int(input("Enter the time in secondss :"))
    def __add__(self,tobj):
        hours=self.__h+tobj2.__h
        print("Sum of hours :",hours)
        minutess=self.__m+tobj2.__m
        print("Sum of minutes :",minutess)
        seconds=self.__s+tobj2.__s
        print("Sum of seconds :",seconds)
        if hours>24:
            hours=hours%24
        if minutess>=60:
            hours=hours+minutess//60
            minutess=minutess%60
        if seconds>=60:
            minutes=minutes+seconds//60
            seconds=seconds%60
        return hours,minutess,seconds
print("Enter the time of first object :")
tobj1=time()
print("Enter the time of second object :")
tobj2=time()
print("Sum of two time is :(hour,minutess,seconds)",tobj1+tobj2)
        
        
        