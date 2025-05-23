# write a python program to get the number from the user , then get the table of the number , and then display the table of the odd numbers only in the reversing order by using function method =>
# number = int(input("Please Enter The Number Is = "))
# def get_table_of_odd_numbers_only(num) :
#     print("The Number Is = ",str(num))
#     print("The Table Of The Number Is : ")
#     for i in range(1 , 11) :
#         print(str(i)+" * "+str(num)+" = "+str(i * num))
#     print("The Table Of The Odd Numbers Only In The Ascending (Properly) Sequence Is : ")
#     for k in range(1 , 11 , 2) :
#         print(str(k)+" * "+str(num)+" = "+str(k * num))
#     print("The Table Of The Odd Numbers Only In The Descending (Reversing) Sequence Is : ")
#     for j in range(11 , -1 , -2) :
#         print(str(j)+" * "+str(num)+" = "+str(j * num))
# get_table_of_odd_numbers_only(number)

def get_table_of_odd_numbers_only(num) :
    print("The Number Is = ",str(num))
    print("The Table Of All Numbers Is : ")
    for i in range(1 , 11) :
            print(str(i)+" * "+str(num)+" = "+str(i * num))
    print("The Table Of The Odd Numbers In The Properly (Ascending) Sequence Only Is : ")
    for k in range(1 , 11) :
        if(k %2 != 0) :
            print(str(k)+" * "+str(num)+" = "+str(k * num))
    print("The Table Of The Odd Numbers Only In The Reversing (Descending) Sequence Is : ")
    for j in range(11 , -1 , -2) :
        if(j %2 != 0) :
            print(str(j)+" * "+str(num)+" = "+str(j * num))
    return("\n")
number = int(input("Please Enter The Number Is = "))
displaying_table_of_odd_numbers_only = get_table_of_odd_numbers_only(number)
print(displaying_table_of_odd_numbers_only)        