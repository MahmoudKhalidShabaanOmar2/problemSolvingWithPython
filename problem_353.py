# write a python program to get list of numbers from the user , and then get the second , and second number from the ending of the list of the numbers , and then get the sum of the second number , and second number from the ending of the list of the numbers by using function method =>
lista_of_numbers = []
number_of_terms = int(input("Please Enter The Number Of Terms Is = "))
print("The Number Of Terms Is = ",str(number_of_terms)," Terms")
for i in range(number_of_terms) :
    numbers = int(input(f"Please Enter The Number {i + 1} Is = "))
    lista_of_numbers.append(numbers)
def get_lista_of_numbers(list_of_nums) :
    print("The List Of The Numbers Is : ",str(lista_of_numbers))
    second_number_from_list_of_numbers = list_of_nums[1]
    print("The Second Number From The List Of The Numbers Is : ",str(second_number_from_list_of_numbers))
    second_number_from_ending_of_list_of_numbers = list_of_nums[-2]
    print("The Second Number From The Ending Of The List Of Numbers Is = ",str(second_number_from_ending_of_list_of_numbers))
    sum_of_second_number_from_starting_ending_of_list_of_numbers = second_number_from_list_of_numbers + second_number_from_ending_of_list_of_numbers 
    print("The Sum Of The Second Number From The Starting Of The List Of Numbers , And The Second Number From The Ending Of The List Of Numbers Is = ",str(sum_of_second_number_from_starting_ending_of_list_of_numbers))
get_lista_of_numbers(lista_of_numbers)    