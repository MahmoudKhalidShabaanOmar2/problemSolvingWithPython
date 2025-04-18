# write a python program to get numbers in a list , and then get the sum of the frist number , and last number from a list of the number => 
lista_of_numbers = []
numbers_of_terms = int(input("Please Enter The Numbers Of Terms Is = "))
print("The Number Of The Terms Is = "+str(numbers_of_terms)+" Terms")
for i in range(numbers_of_terms) :
    numbers = int(input("Please Enter All Numbers To Store In The List Of The Numbers Is = "))
    lista_of_numbers.append(numbers)
print("The List Of All Numbers Is : "+str(lista_of_numbers))
frist_number_from_lista_of_numbers = lista_of_numbers[0]
print("The Frist Number From The List Of The Numbers Is = "+str(frist_number_from_lista_of_numbers))
last_number_from_lista_of_numbers = lista_of_numbers[-1]
print("The Last Number From The List Of The Number Is = "+str(last_number_from_lista_of_numbers))
sum_of_frist_last_number_from_lista_of_numbers = frist_number_from_lista_of_numbers + last_number_from_lista_of_numbers 
print("The Sum Of The Frist Number , And The Last Number From The List Of The Numbers Is = "+str(sum_of_frist_last_number_from_lista_of_numbers))