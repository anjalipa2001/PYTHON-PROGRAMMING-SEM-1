text="I'm a programmer and I'm a student"
words={}
text=text.split(" ")
for word in text:
    if word in words:
        words[word]+=1
    else:
            words[word]=1
print(words)