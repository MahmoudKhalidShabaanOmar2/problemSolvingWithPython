# write a python program to get the list of numbers from the user , and then get the middle number from the list of number , and at the end get the square root of the middle number from the list of numbers =>
import math 
lista_of_numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15]
print("The List Of Numbers Is : "+str(lista_of_numbers))
length_of_list_of_numbers = len(lista_of_numbers)
print("The Length Of The List Of Numbers Is = "+str(length_of_list_of_numbers)+" Numbers")
half_number = length_of_list_of_numbers / 2
middle_number = int(half_number)
middle_number_from_list_of_numbers = lista_of_numbers[middle_number]
print("The Middle Number From The List Of The Numbers Is = ",str(middle_number_from_list_of_numbers))
square_root_of_middle_number_from_list_of_numbers = math . sqrt(middle_number_from_list_of_numbers)
print("The Square Root Of The Middle Number From The List Of Numbers Is = ",str(square_root_of_middle_number_from_list_of_numbers))