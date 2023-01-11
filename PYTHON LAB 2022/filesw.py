fn=open("para.txt","w")
fn.write("Python is a great language \n Yeah its great\n")
fn.close()

fn=open("para.txt","r")
str=fn.read(1);
print("Read string is : ",str)
fn.close()
