#Display future leap years from current year to a final year entered by user. 
y=int(input("Enter the last year :"))
print("Leap years are :")
for i in range(2024,y,4):
    i%4==0
    print(i)