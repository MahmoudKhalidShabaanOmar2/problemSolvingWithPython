# write a python program to get the list of the numbers , and then get the cube of the numbers by using list comprehension method by using function method =>
numbers_of_terms = int(input("Please Enter The Number Of Terms Is = "))
lista_of_numbers = []
def get_new_lista_of_numbers(nums_of_terms , lst_of_nums):
    print("The Number Of Terms Is = ",str(nums_of_terms)," Terms")
    for i in range(nums_of_terms):
        number = int(input(f"Please Enter The Number {i + 1} Is = "))
        lst_of_nums.append(number)
    print("The List Of The Numbers Is : ",str(lst_of_nums))
    # new_lista_of_numbers = [num * num * num for num in lst_of_nums]
    # new_lista_of_numbers = [pow(num , 3) for num in lst_of_nums]
    new_lista_of_numbers = [num ** 3 for num in lst_of_nums]
    print("The New List Of Numbers Is : ",str(new_lista_of_numbers))
get_new_lista_of_numbers(numbers_of_terms , lista_of_numbers)