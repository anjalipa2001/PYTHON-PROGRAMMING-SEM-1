'''import random
list=['alby','ancy','basil','benny']
print(random.choices(list))
print(random.choices(list,k=4))
print(random.sample(list,k=2))
random.shuffle(list)
print(list)
print(random.randrange(3,8))'''

''''
import time
print("Current time in sec:",time.time())
print("Current time :",time.ctime())
print("Current time after 30sec :",time.ctime(time.time()+30))
t=time.localtime()
print("time t :",t)
print("Current year : ",t.tm_year)
print("Current month : ",t.tm_mon)
print("Current day : ",t.tm_mday)
print("Current week : ",t.tm_wday)
print("Current hour : ",t.tm_hour)

import math 
print("pi value :",math.pi)
from math import pi,sqrt
print("pi value :",pi)
print("sqrt of 169:",sqrt(169))
print()
print(math.cos(90))
print(math.sin(30))'''
 
import statistics as s
m=[20,30,40,50,60]
print("median : ",s.median(m))
print("mode : ",s.mode(m))
print("mean : ",s.mean(m))
print("variance : ",s.variance(m))
print("harmonic mean: ",s.harmonic_mean(m))
print(s.median_low([-11,5,-4.5,6,9]))



