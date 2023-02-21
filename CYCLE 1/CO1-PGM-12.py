#Accept a file name from user and print extension of that
filename=input("Enter the Filename :")
ext=filename.split(".")
print("Extension of the file is "+ext[-1])