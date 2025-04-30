# write a python program to get list of numbers from the user , and then get the second number from the end of the list of the numbers =>
lista_of_numbers = []
numbers_of_terms = int(input("Please Enter The Numbers Of Terms Is = "))
print("The Number Of Terms Is = ",numbers_of_terms," Terms")
for i in range(numbers_of_terms) :
    numbers = int(input(f"Please Enter The Number {i + 1} To Store In The List Of The Numbers Is = "))
    lista_of_numbers.append(numbers)
print("The List Of The Numbers Is : ",str(lista_of_numbers))
# second_number_from_ending_of_list_of_numbers = lista_of_numbers[-2]
second_number_from_ending_of_list_of_numbers = lista_of_numbers[numbers_of_terms - 2]
print("The Second Number From The Ending Of The List Of The Numbers Is = ",str(second_number_from_ending_of_list_of_numbers))