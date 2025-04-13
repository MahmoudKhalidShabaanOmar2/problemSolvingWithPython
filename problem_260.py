# write a python program to get numbers from the user , then store all numbers in a tuple to check if the frist number and the lasr number from the tuple of numbers is the same numbers or not the same numbers =>
lista_of_numbers = []
number_of_terms = int(input("Please Enter The Number Of The Terms Is = "))
for i in range(number_of_terms) :
    numbers = int(input("Please Enter All Numbers To Store In The List Of The Numbers Is = "))
    lista_of_numbers.append(numbers) 
print("\nThe List Of The Numbers Is : ")
print(lista_of_numbers)
tuples_of_numbers = tuple(lista_of_numbers)
print("\nThe Tuple Of The Number Is = ")
print(tuples_of_numbers)
if((tuples_of_numbers[0] == tuples_of_numbers[number_of_terms - 1])) :
    print("The Frist Number Is The Same The Last Number From The Tuple Of The Numbers")
    print(tuples_of_numbers)
else :
    print("The Frist Number Is Not The Same Of The Last Number From The Tuple Of The Number")
    print(tuples_of_numbers)