# write a python program to get the table of the numbers , the system should display only odd numbers in the reverse order =>
# number = int(input("Please Enter The Number Is = "))
# print("The Number Is = ",str(number))
# print("Generating The Table Of The Number Of Only ODD Numbers In The Descending (Reversing) Order Is : ")
# for num in range(11 , 1 , -2) :
#     print(str(num)+" * "+str(number)+" = "+str(num * number))

number = int(input("Please Enter The Number Is = "))
print("The Number Is = ",str(number))
print("Generating The Table Of The Number Of Only ODD Numbers In The Descending (Reversing) Order Is : ")
for num in range(11 , 1 , -2) :
    if(num %2 != 0) :
        print(str(num)+" * "+str(number)+" = "+str(num * number))