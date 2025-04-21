# write a python program to get number from the user , decremented half number from the user , the system should add auto decrement to that number , half of user entered number should be decremented => 
number = int(input("Please Enter The Number Is = "))
print("The Number Is = ",str(number))
half_count_number = number // 2
print("The Half Count Number Is = ",str(half_count_number))
print(f"\nAuto Decremented Number Of (Count {half_count_number}) Is : ")
for i in range(half_count_number) :
    print(number - i)