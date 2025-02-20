# write a python program to get five colors name from the user in list , and then display that list , remove the frist color , and then display all colors for the user =>
lista_of_different_colors = []
# for i in range(5) :
    # lista_of_different_colors . append(input("please enter the different colors name to store in the list of the colors name is : "))
lista_of_different_colors = [input("please enter the different colors name to store in the list of the different colors name is : ") for i in range(5)]
print("the list of the different colors name before removing the frist color name is : "+str(lista_of_different_colors))
print("the length of the list of the different colors name before removing the last frist name is = "+str(len(lista_of_different_colors))+" colors")
# lista_of_different_colors . pop(0)
lista_of_different_colors . remove(lista_of_different_colors[0])
print("the list of the differnet colors name after removing the frist color name is : "+str(lista_of_different_colors))
print("the length of the list of the different colors name after removing the frist color name is = "+str(len(lista_of_different_colors))+" colors")