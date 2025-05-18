# write a python program to get number from the user , and then subtract the half of the number by using function methods =>
number = int(input("Please Enter The Number Is = "))
def get_number(num) :
    print("The Number Is = ",str(num))
    half_count_number = num // 2
    print("The Half Count Number Is = ",str(half_count_number))
    for i in range(half_count_number) :
        subtract_number_from_half_count_number = num - i 
        print(f"The Subtraction Of The Number From The Half Number ({num} - {i}) Is = ",str(subtract_number_from_half_count_number))
get_number(number)