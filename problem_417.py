# write a python program to count any item from a nested list =>
import math
nested_lista_of_numbers = [[1 , 2 , 3 , 4 , 5 , 12] , [4 , 3 , 2 , 6 , 4 , 7]]
print("The Nested List Of The Numbers Is : ",str(nested_lista_of_numbers))
number = int(input("Please Enter The Number Is = "))
print("The Number Is = ",str(number))
result_of_count_number = sum(num.count(number) for num in nested_lista_of_numbers)
print("The Count Of The Number Is = ",str(result_of_count_number))