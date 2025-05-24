# write a python program to get the table of the number , and then get the table of the even numbers only by using function method =>
# number = int(input("Please Enter The Number Is = "))
# def get_table_of_even_numbers_only(num) :
#     print("The Number Is = ",str(num))
#     print("The Table Of The Number Is : ")
#     for i in range(0 , 12) :
#         print(str(i)+"* "+str(num)+" = "+str(i * num))
#     print("The Table Of The Even Numbers Only In The Ascending (Properly) Sequence Is : ")
#     for j in range(0 , 13 , 2) :
#         print(str(j)+" * "+str(num)+" = "+str(j * num))
#     print("The Table Of The Odd Numbers Only In The Descending (Reversing) Sequence Is : ")
#     for k in range(12 , 0 , -2) :
#         print(str(k)+" * "+str(num)+" = "+str(k * num))
# get_table_of_even_numbers_only(number)

def get_table_of_even_numbers_only(num) :
    print("The Number Is = ",str(num))
    print("The Table Of The Number Is : ")
    for i in range(0 , 13) :
        print(str(i)+" * "+str(num)+" = "+str(i * num))
    print("The Table Of The Even Numbers Only In The Ascending (Properly) Sequence Is : ")
    for k in range(0 , 13) :
        if(k %2 == 0) :
            print(str(k)+" * "+str(num)+" = "+str(k * num))
    print("The Table Of The Even Numbers Only In The Descending (Reversing) Sequence Is : ")
    for j in range(12 , 0 , -2) :
        print(str(j)+" * "+str(num)+" = "+str(j * num))
    return("\n")
number = int(input("Please Enter The Number Is = "))
displaying_table_of_even_numbers_only = get_table_of_even_numbers_only(number)
print(displaying_table_of_even_numbers_only)