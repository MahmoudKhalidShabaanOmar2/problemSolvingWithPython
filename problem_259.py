# write a python program to get different numbers in a list , then display list of all numbers , and at the end display only numbers that divisible by three , and five from a list of numbers =>
lista_of_numbers = []
number_of_terms = int(input("Please Enter The Number Of Terms Is = "))
for i in range(number_of_terms) :
    numbers = int(input(f"Please Enter All Numbers To Store In The List Of The Numbers {i + 1} Is = "))
    lista_of_numbers.append(numbers)
print("\nThe List Of All Numbers Is : ")
print(lista_of_numbers)
print("\nAll Numbers That Divisible By Three , And Five From The List Of The Numbers Is : ")
# numbers_divisible_by_3_5 = [numbers for numbers in lista_of_numbers if((numbers %3 == 0) and (numbers %5 == 0))] 
for numbers in lista_of_numbers :
    if(numbers %3 == 0 and numbers %5 == 0) :
        print(numbers)
# print(numbers_divisible_by_3_5) 