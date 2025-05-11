# write a python program to get list of numbers from the user , and then display the frist , and last numbers from the list of the numbers , and at the end get the sum of the frist , and last numbers from the list of numbers by using function method =>
lista_of_numbers = []
numbers_of_terms = int(input("Please Enter The Numbers Of Terms Is = "))
def get_lista_of_numbers(num_of_terms , list_of_nums) :
    print("The Number Of Terms Is = ",str(num_of_terms)," Terms")
    for i in range(num_of_terms) :
        numbers = int(input(f"Please Enter The Number {i + 1} Is = "))
        lista_of_numbers.append(numbers)
    print("The List Of All Numbers Is : ",str(list_of_nums))
    frist_number_from_list_of_numbers = list_of_nums[0]
    print("The Frist Number From The List Of Numbers Is = ",str(frist_number_from_list_of_numbers))
    # last_number_from_list_of_numbers = list_of_nums[-1] 
    last_number_from_list_of_numbers = num_of_terms -1 
    print("The Last Number From The List Of Numbers Is = ",str(last_number_from_list_of_numbers))
    sum_of_frist_number_last_number_from_list_of_numbers = frist_number_from_list_of_numbers + last_number_from_list_of_numbers 
    print("The Sum Of The Frist Number , And Last Number From The List Of All Numbers Is = ",str(sum_of_frist_number_last_number_from_list_of_numbers))
get_lista_of_numbers(numbers_of_terms , lista_of_numbers)