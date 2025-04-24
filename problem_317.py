# write a python program to get number from the user to display the table of the number in the reversing order => 
number = int(input("Please Enter The Number Is = "))
print("The Number Is = ",str(number))
print("Displaying The Table Of The Number In The Properly (Ascending) Order Is : ")
for i in  range(0 , 11) :
    print(str(number) + " * "+str(i) + " = "+str(number * i))
print("Displaying The Table Of The Number In The Descending (Reversing) Order Is : ")
for j in range(11 , 0 , -1) :
    print(str(number)+" * "+str(j)+" = "+str(number * j))