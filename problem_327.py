# write a python program to get the list of the numbers to get the middle number from the list of the numbers , and then get the square of the middle number from the list of the numbers =>
lista_of_numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15]
print("The List Of Numbers Is : ",str(lista_of_numbers))
length_of_lista_of_numbers = len(lista_of_numbers)
print("The Length Of The List Of Numbers Is = ",str(length_of_lista_of_numbers)," Numbers")
half_number = length_of_lista_of_numbers / 2
middle_number = int(half_number)
middle_number_from_lista_of_numbers = lista_of_numbers[middle_number]
print("The Middle Number From The List Of Numbers Is = ",str(middle_number_from_lista_of_numbers))
# square_of_middle_number_from_lista_of_numbers = middle_number_from_lista_of_numbers * middle_number_from_lista_of_numbers 
# square_of_middle_number_from_lista_of_numbers = pow(middle_number_from_lista_of_numbers , 2)
square_of_middle_number_from_lista_of_numbers = middle_number_from_lista_of_numbers ** 2
print("The Square Of The Middle Number From The List Of The Numbers Is = ",str(square_of_middle_number_from_lista_of_numbers))