# write a python program to get list of numbers from the user , and then get the second number from the end of list of the numbers , and at the end get square root of the second number from the end of the list of the numbers =>
import math 
lista_of_numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15]
print("The List Of The Numbers Is : "+str(lista_of_numbers))
length_of_list_of_numbers = len(lista_of_numbers)
print("The Length Of The List Of The Numbers Is = ",str(length_of_list_of_numbers)," Numbers")
second_number_from_ending_of_list_of_numbers = lista_of_numbers[-2]
print("The Second Number From The Ending Number From The List Of The Numbers Is = ",str(second_number_from_ending_of_list_of_numbers))
square_root_of_second_number_from_ending_of_list_of_numbers = math . sqrt(second_number_from_ending_of_list_of_numbers)
print("The Square Of The Second Number From The Ending Of The List Of The Numbers Is = ",square_root_of_second_number_from_ending_of_list_of_numbers)