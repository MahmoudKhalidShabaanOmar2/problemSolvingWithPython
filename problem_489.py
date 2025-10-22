# write a python program to get list of numbers from the user , and then get the minimum number from the list of all numbers by using list comprehension by using function method =>
numbers_of_terms = int(input("Please Enter The Number Of Terms Is = "))
lista_of_numbers = []
def get_minimum_number_between_list_number(nums_of_terms , list_of_nums):
    print("The Number Of Terms Is = ",str(nums_of_terms)," Terms")
    for i in range(nums_of_terms):
        number = int(input(f"Please Enter The Number {i + 1} Is = "))
        list_of_nums.append(number)
    print("The List Of All Numbers Is : ",str(list_of_nums))
    minimum_number_between_list_numbers = min([num for num in list_of_nums])
    print("The Minimum Number Between List Numbers Is = ",str(minimum_number_between_list_numbers))
get_minimum_number_between_list_number(numbers_of_terms , lista_of_numbers)