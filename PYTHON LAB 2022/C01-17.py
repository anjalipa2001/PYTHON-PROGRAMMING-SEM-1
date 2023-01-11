dic={
    "Bob":24,
    "Charlie":36,
    "Alice":72,
    "Eric":18,
    "David":9,
    }
s=sorted(dic.items())
print("Ascending order \n",s)
s1=sorted(dic.items(),reverse=True)
print("Descending order \n",s1)
