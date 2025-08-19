# write a python program to access multiple elements from the tuple of different elements =>
lista_of_elements = [1 , 2 , 53 , -454 , 65 , -4646 , 6454.454 , 646443.3434 , -353.34343 , -5334.3535 , True , False , "Ahmed" , "Mohamed"]
print("The List Of Different Elements Is : ",str(lista_of_elements))
tuples_of_elements = tuple(lista_of_elements)
print("The Tuple Of Different Elements Is : ",str(tuples_of_elements))
starting_position = int(input("Please Enter The Starting Position Is = "))
print("The Starting Position Is = ",str(starting_position))
ending_position = int(input("Please Enter The Ending Position Is = "))
print("The Ending Position Is = ",str(ending_position))
ending_element = ending_position + 1
print("Access Multiple Elements From The Tuples Of Different Elements Is : ")
print(tuples_of_elements[starting_position:ending_element])