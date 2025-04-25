# write a python program to get number from the user , and then get the table of the number of only EVEN numbers in the reversing order =>
# number = int(input("Please Enter The Number Is = "))
# print("The Number Is = ",str(number))
# print("Generating The Table Of The Number Of Only EVEN Numbers In The Reversing (Descending) Order Is : ")
# for num in range(10 , 0 , -2) :
#     print(str(num)+" * "+str(number)+" = "+str(num * number))

number = int(input("Please Enter The Number Is = "))
print("The Number Is = ",str(number))
print("Generating Table Of The Number Of Only EVEN Numbers In The Descending Order Is : ")
for num in range(10 , 0 , -2) :
    if(num %2 == 0) :
        print(str(num)+" * "+str(number)+" = "+str(num * number))