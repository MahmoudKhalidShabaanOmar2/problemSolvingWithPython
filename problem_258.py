# write a python program to get numbers in a list , and then display all numbers in the list , and at the end display only numbers that divisible by three from the list of the different numbers =>
lista_of_numbers = []
number_of_terms = int(input("Please Enter The Number Of Terms Is = "))
for i in range(number_of_terms) : 
    numbers = int(input(f"Please Enter All Numbers To Store In The List Of The Numbers {i + 1} Is = "))
    lista_of_numbers.append(numbers)
print("The List Of The Numbers Is = "+str(lista_of_numbers))
numbers_divisible_by3 = [numbers for numbers in lista_of_numbers if(numbers %3 == 0)] 
print("\nAll Numbers Divisible By Three From The List Of The Numbers Is : \n")
print(numbers_divisible_by3)