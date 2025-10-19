# write a python program to get the list of numbers from the user , and then get the cube of all numbers by using list comperhension mthod =>
number_of_terms = int(input("Please Enter The Number Of Terms Is = "))
print("The Number Of Terms Is = ",str(number_of_terms)," Terms")
lista_of_numbers = []
for i in range(number_of_terms):
    number = int(input(f"Please Enter The Number {i + 1} Is = "))
    lista_of_numbers.append(number)
print("The List Of The Number Is : ",str(lista_of_numbers))
new_lista_of_numbers = [num * num * num for num in lista_of_numbers]
print("The New List Of Numbers Is : ",str(new_lista_of_numbers))