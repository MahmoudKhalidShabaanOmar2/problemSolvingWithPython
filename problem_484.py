# write a python program to get the list of numbers , and then get the square root of all numbers from the list of numbers =>
import math 
numbers_of_terms = int(input("Please Enter The Number Of Terms Is = "))
print("The Number Of Terms Is = ",str(numbers_of_terms))
lista_of_numbers = []
for i in range(numbers_of_terms):
    number = int(input(f"Please Enter The Number {i + 1} Is = "))
    lista_of_numbers.append(number)
print("The List Of The Numbers Is : ",str(lista_of_numbers))
square_root_of_all_numbers_from_list = [math.sqrt(num) for num in lista_of_numbers]
print("The Square Rooy Of All Numbers From The List Is : ",str(square_root_of_all_numbers_from_list))