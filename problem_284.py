# write a python program to get numbers from the user in a list of numbers , and then get the sum of second number from frist , and second number from last from the list of the numbers => 
lista_of_numbers = []
numbers_of_terms = int(input("Please Enter The Numbers Of Terms Is = "))
print("The Numbers Of Terms Is = ",str(numbers_of_terms)+" terms")
for i in range(numbers_of_terms) :
    numbers = int(input("Please Enter All Numbers To Store In The List Of The Numbers Is = "))
    lista_of_numbers . append(numbers)
print("The List Of The Numbers Is = "+str(lista_of_numbers))
second_number_from_frist_of_lista_of_numbers = lista_of_numbers[1]
print("The Second Number From The Frist Of The List Of Numbers Is = "+str(second_number_from_frist_of_lista_of_numbers))
second_number_from_last_of_lista_of_numbers = lista_of_numbers[-2]
print("The Second Number From The Last Of The List Of Numbers Is = "+str(second_number_from_last_of_lista_of_numbers))
sum_of_second_number_from_frist_last_of_lista_of_numbers = second_number_from_frist_of_lista_of_numbers + second_number_from_last_of_lista_of_numbers
print("The Sum Of The Second Number From The Frist Of The List Of Numbers , And The Second Number From The Last Of The List Of Numbers Is ="+str(sum_of_second_number_from_frist_last_of_lista_of_numbers))