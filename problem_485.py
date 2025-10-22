# write a python program to get the list of  numbers , and then get the square root of all numbers from the list by using list comprehension by using function method =>
import math
numbers_of_terms = int(input("Please Enter The Number Of Terms Is = "))
lista_of_numbers = []
def get_square_root_of_numbers_from_list(list_of_nums , nums_of_terms):
    print("The Numbers Of Terms Is = ",str(nums_of_terms)," Terms")
    for i in range(nums_of_terms):
        number = int(input(f"Please Enter The Number {i + 1} Is = "))
        list_of_nums.append(number)
    print("The List Of All Numbers Is : ",str(list_of_nums))
    new_lista_of_numbers = [math.sqrt(num) for num in list_of_nums]
    print("The New List Of All Numbers Is : ",str(new_lista_of_numbers))
get_square_root_of_numbers_from_list(lista_of_numbers , numbers_of_terms)