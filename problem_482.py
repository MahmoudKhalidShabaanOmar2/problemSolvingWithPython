# write a python program to get the list of numbers from the user , and then get the sum of all numbers from the list of numbers by using list comprehension method =>
numbers_of_terms = int(input("Please Enter The Numbers Of Terms Is = "))
print("The Number Of Terms Is = ",str(numbers_of_terms)," Terms")
lista_of_numbers = []
for i in range(numbers_of_terms):
    number = int(input(f"Please Enter The Number {i + 1} Is = "))
    lista_of_numbers.append(number)
print("The List Of All Numbers Is : ",str(lista_of_numbers))
sum_of_all_numbers_from_list = sum([num for num in lista_of_numbers])
print("The Sum Of All NUmbers From The List Is = ",str(sum_of_all_numbers_from_list))