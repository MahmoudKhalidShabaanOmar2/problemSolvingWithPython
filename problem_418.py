# write a python program to print the list from a nested list which have lowest number =>
nested_lista_of_numbers = [[1 , 3 , 2 , 4 , 5] , [5 , 6 , 7 , 2 , 1 , 6] , [8 , 9 , 10 , 45 , 34 ,24]]
print("The Nested List Of Numbers Is : ",str(nested_lista_of_numbers))
lowest_list_of_numbers_from_nested_list_of_numbers = min(nested_lista_of_numbers , key=lambda sublist: min(sublist))
print("The Lowest List Of Numbers From The Nested List Of Numbers Is : ",str(lowest_list_of_numbers_from_nested_list_of_numbers))
min_number_from_lowest_list_of_numbers = min(lowest_list_of_numbers_from_nested_list_of_numbers)
print("The Lowest Number From The Lowest List Of Numbers Is = ",str(min_number_from_lowest_list_of_numbers))