# write a python program to get the list of numbers from the user , and then get the maximum number between the list numbers by using function method =>
numbers_of_terms = int(input("Please Enter The Numbers Of Terms Is = "))
lista_of_numbers = []
def get_maximum_number_between_list_numbers(nums_of_terms , list_of_nums):
    print("The List Of All Numbers Is = ",str(nums_of_terms)," Terms")
    for i in range(nums_of_terms):
        number = int(input(f"Please Enter The Number {i + 1} Is = "))
        list_of_nums.append(number)
    print("The List Of All Numbers Is = ",str(list_of_nums))
    maximum_number_between_list_numbers = max([num for num in list_of_nums])
    print("The Maximum Number Between The List Of All Numbers Is = ",str(maximum_number_between_list_numbers))
get_maximum_number_between_list_numbers(numbers_of_terms , lista_of_numbers)