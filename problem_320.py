# write a python program to get the table of the numbers , the system should generate only the table of Even Number => 
# number = int(input("Please Enter The Number Is = "))
# print("The Number Is = ",str(number))
# print("Generating The Table Of The Number Of Only EVEN Numbers Is : ")
# for num in range(0 , 11 , 2) :
#     print(str(num)+" * "+str(number)+" = "+str(num * number))

number = int(input("Please Enter The Number Is = "))
print("The Number Is = ",str(number))
print("Generating The Table Of Number Of The Even Numbers Only Is : ")
for num in range(0 , 11) :
    if(num %2 == 0) :
        print(str(num)+" * "+str(number)+" = "+str(num * number))