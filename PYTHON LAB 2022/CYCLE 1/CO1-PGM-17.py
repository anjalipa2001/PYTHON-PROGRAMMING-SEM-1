# Sort dictionary in ascending and descending order.
dic={
    "Bob":23,
    "Charlie":44,
    "Alice":72,
    "Emy":18,
    "David":19,
    }
s=sorted(dic.items())
print("Ascending Order :",s)
s1=sorted(dic.items(),reverse=True)
print("Descending Order :",s1)