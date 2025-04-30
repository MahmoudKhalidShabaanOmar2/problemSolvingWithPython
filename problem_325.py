# write a python program to get numbers from the user in a list , and then get the middle number from the list =>
lista_of_numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
print("The List Of The Numbers Is : "+str(lista_of_numbers))
length_of_lista_of_numbers = len(lista_of_numbers)
print("The Length Of The List Of Numbers Is = ",str(length_of_lista_of_numbers)," Numbers")
half_number = length_of_lista_of_numbers / 2
middle_number = int(half_number)
middle_number_from_lista_of_numbers = lista_of_numbers[middle_number]
print("The Middle Number From The List Of Numbers Is = ",str(middle_number_from_lista_of_numbers))