# write a python program to get list of numbers from the user , and then get the square of all numbers by using list comprehension method =>
numbers_of_terms = int(input("Please Enter The Number Terms Is = "))
print("The Number Of Terms Is = ",str(numbers_of_terms)," Terms")
lista_of_numbers = []
for i in range(numbers_of_terms):
    number = int(input(f"Please Enter The Number {i + 1} Is = "))
    lista_of_numbers.append(number)
print("The List Of Numbers Is : ",str(lista_of_numbers))
# new_lista_of_numbers = [num * num for num in lista_of_numbers]
# new_lista_of_numbers = [num ** 2 for num in lista_of_numbers]
new_lista_of_numbers = [pow(num , 2) for num in lista_of_numbers]
print("The New List Of Numbers Is : ",str(new_lista_of_numbers))