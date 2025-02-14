# write a python program to get six numbers in tuple ,and display tuple , and then clear all numbers from the tuple and clear the tuple , and then display =>
lista_of_numbers = []
for i in range(6) :
    lista_of_numbers . append(int(input("please enter the numbers to store in the list of the numbers is = ")))
print("the list of the numbers before clearing all numbers from the list is = "+str(lista_of_numbers))
tuple_of_numbers = tuple(lista_of_numbers)
print("the tuple of the numbers is = "+str(tuple_of_numbers))
lista_of_numbers . clear()
print("the list of the numbers after clearing all numbers from the list is = "+str(lista_of_numbers))
tuple_of_numbers = tuple(lista_of_numbers)
print("the tuple of the numbers aftering clearing all numbers from the tuple is = "+str(tuple_of_numbers))
