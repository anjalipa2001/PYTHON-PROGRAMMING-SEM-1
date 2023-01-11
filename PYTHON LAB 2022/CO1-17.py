dic={
    "Bob": 24,
    "Charlie": 36,
    "Alice": 72,
    "Eric": 18,
    "David": 9
     }
s1 = sorted(dic.items())#key=lambda x: x[1])
print("Dictionary in Ascending order :",s1)
s2=sorted(dic.items(),reverse=True)
print(s2)
