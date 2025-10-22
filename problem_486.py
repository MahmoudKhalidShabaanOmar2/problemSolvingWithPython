# write a python to get the list of numbers from the user , and then get the maaximum number between different numbers in the list by using the list comprehension =>
numbers_of_terms = int(input("Please Enter The Numbers Of Terms Is = "))
print("The Numbers Of Terms Is = ",str(numbers_of_terms)," Terms")
lista_of_numbers = []
for i in range(numbers_of_terms):
    number = int(input(f"Please Enter The Number {i + 1} Is = "))
    lista_of_numbers.append(number)
print("The List Of All Numbers Is : ",str(lista_of_numbers))
maximum_number_between_list_numbers = max([num for num in lista_of_numbers])
print("The Maximum Number Between List Of All Numbers Is = ",str(maximum_number_between_list_numbers))