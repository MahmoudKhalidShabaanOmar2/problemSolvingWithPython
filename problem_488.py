# write a python program to get the list of all numbers and then get the minimum number between all numbers in the list of all numbers by using the list comprehension =>
numbers_of_terms = int(input("Please Enter The Number Of Terms Is = "))
print("The Number Of Terms Is = ",str(numbers_of_terms)," Terms")
lista_of_numbers = []
for i in range(numbers_of_terms):
    number = int(input(f"Please Enter The Number {i + 1} Is = "))
    lista_of_numbers.append(number)
print("The List Of All Numbers Is : ",str(lista_of_numbers))
minimum_number_between_list_numbers = min([num for num in lista_of_numbers])
print("The Minimum Number From The List Of All Numbers Is = ",str(minimum_number_between_list_numbers))