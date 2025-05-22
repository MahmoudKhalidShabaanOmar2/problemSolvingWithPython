# write a python program to get number from the user to get the table of the number , and then should the number should multiply of the odd numbers only by using function method =>
# number = int(input("Please Enter The Number Is = "))
# def get_table_of_odd_numbers_only(num) :
#     print("The Number Is = ",str(num))
#     print("The Table Of All Number Is : ")
#     for i in range(1 , 11) :
#         print(str(i)+" * "+str(num)+" = "+str(i * num))
#     print("The Table Of The Odd Number Only Is : ")
#     for k in range(1 , 11 , 2) :
#         print(str(k)+" * "+str(num)+" = "+str(num * k))
# get_table_of_odd_numbers_only(number)

number = int(input("Please Enter The Number Is = "))
def get_table_of_odd_numbers_only(num) :
    print("The Number Is = ",str(num))
    print("The Table Of All Numbers Is : ")
    for i in range(1 , 11) :
        print(str(i)+" * "+str(num)+" = "+str(i * num))
    print("The Table Of The Odd Numbers Only Is : ")
    for k in range(1 , 11) :
        if(k %2 != 0) :
            print(str(k)+" * "+str(num)+" = "+str(k * num))
get_table_of_odd_numbers_only(number)