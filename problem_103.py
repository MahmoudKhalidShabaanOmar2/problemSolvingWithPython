# write a python program to get five colors name from the user in list , display that list of colors name , remove last color name , and then display all colors name for the user =>
lista_of_colors = []
# for i in range(5) :
    # lista_of_colors . append(input("please enter the different colors to store in the list of the different colors is : "))
lista_of_colors = [input("please enter the different colors name to store in the list of the different colors name is : ") for i in range(5)]
print("the list of the different colors name before removing the last color name  is : "+str(lista_of_colors))
print("the length of the list of the different colors name before removing the last color name is : "+str(len(lista_of_colors))+" colors")
# lista_of_colors . pop()
# lista_of_colors . pop(4)
# lista_of_colors . pop(-1)
# lista_of_colors . remove(lista_of_colors[4])
lista_of_colors . remove(lista_of_colors[-1])
print("the list of the different colors name after removing the last color name is = "+str(lista_of_colors))
print("the length of the list of the different colors name after removing the last color name is "+str(len(lista_of_colors))+" colors")