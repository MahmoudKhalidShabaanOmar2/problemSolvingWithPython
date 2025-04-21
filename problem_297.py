# write a python program to get number from the user , the system should add auto increment to that number half of user entered number should be incremented =>
number = int(input("Please Enter The Number Is = "))
print("The Number From The User Is = ",str(number))
half_count_number = number // 2
print("The Half Count Number Is = ",str(half_count_number))
for i in range(half_count_number) :
    print(i + number)