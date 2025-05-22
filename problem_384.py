# write a python program to get the number from the user , and then get the table of the number in the reversing order by using function method =>
number = int(input("Please Enter The Number Is = "))
def get_table_of_number(num) :
    print("The Number Is = ",str(num))
    print("The Table Of The Number In The Ascending (Properly) Sequence Is : ")
    for n in range(1 , 11) :
        print(str(n)+" * "+str(num)+" = "+str(n * num))
    print("The Table Of The Number In The Reversing (Descending) Sequence Is : ")    
    for k in range(11 , 0 , -1) :
        print(str(k)+" * "+str(num)+" = "+str(k * num))
get_table_of_number(number)