# write a python program to find the most occuring from the given list of numbers =>
import statistics
from statistics import mode 
lista_of_numbers = [1 , 2 , 3 , 4 , 1 , 5 , 6 , 334 , 5 , 33 , 53 , 1 , 5 , 2 , 8 , 9 , 1]
print("The List Of The Numbers Is : "+str(lista_of_numbers))
most_ocurring_number = mode(lista_of_numbers)
print("The Most Ocurring Number From The List Of The Numbers Is = "+str(most_ocurring_number))