# write a python program to get six numbers from the user in the list , and display all numbers and then clear , and then display =>
# lista_of_numbers = []
# for i in range(6) :
    # lista_of_numbers . append(int(input("please enter the numbers to store in the list of the numbers is = ")))
lista_of_numbers = [int(input("please enter the numbers to store in the list of the numbers is = ")) for i in range(6)]
print("the list of the numbers before clearing all numbers from the list of the numbers is = "+str(lista_of_numbers))
lista_of_numbers . clear()
print("the list of the numbers after clearing all numbers from the list of the numbers is = "+str(lista_of_numbers))