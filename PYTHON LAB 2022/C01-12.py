#Accept a file name from user and print extension of that
filename = input("Input the Filename: ")
extsn = filename.split(".")
print ("The extension of the file is : " + repr(extsn[1]))