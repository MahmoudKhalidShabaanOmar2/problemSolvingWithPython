# write a python program to get the list from the user , and then get the sum of all numbers from the list by using list comperhension method by using function method =>
numbers_of_terms = int(input("Please Enter The Number Of Terms Is = "))
lista_of_numbers = []
def get_sum_of_all_numbers_from_list(nums_of_terms , lst_of_nums):
    print("The Number Of Terms Is = ",str(nums_of_terms)," Terms")
    for i in range(nums_of_terms):
        number = int(input(f"Please Enter The Number {i + 1} Is = "))
        lst_of_nums.append(number)
    print("The List Of All Numbers Is : ",str(lst_of_nums))
    sum_of_all_numbers_from_list = sum([num for num in lst_of_nums])
    print("The Sum Of All Numbers From The List Is = ",str(sum_of_all_numbers_from_list))
get_sum_of_all_numbers_from_list(numbers_of_terms , lista_of_numbers)