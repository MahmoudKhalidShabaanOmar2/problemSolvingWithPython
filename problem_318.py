# write a python program to get number from the user to display table , number should multiply with odd numbers only => 
# number = int(input("Please Enter The Number Is = "))
# print("The Number Is = ",str(number))
# print("Generating Table Of The Number Of Only ODD Numbers Is : ")
# for num in range(1 , 11 , 2) :
#     print(str(num)+" * "+str(number)+" = "+str(number * num))

number = int(input("Please Enter The Number Is = "))
print("The Number Is = ",str(number))
print("Generating The Table Of The Number Of Only ODD Numbers Is : ")
for num in range(1 , 11) :
    if(num %2 != 0) :
        print(str(num)+" * "+" = "+str(number)+" = "+str(number * num))