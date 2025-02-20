# write a python program to get five colors name from the user in list , and then display that list , remove the frist color , and then display all colors for the user by using different function methods =>
# lista_of_different_colors = []
# # for i in range(5) :
#     # lista_of_different_colors . append(input("please enter the different colors to store in the list of the different colors is : "))
# lista_of_different_colors = [input("please enter the different colors name to store in the list of the different colors name is : ") for i in range(5)]
# def get_lista_of_different_colors_name(list_of_colors) :
#     print("the list of the different colors name before removing the frist color name is : "+str(list_of_colors))
#     print("the length of the list of the different colors name before removing the frist color name is = "+str(len(list_of_colors))+" colors")
#     # list_of_colors . remove(list_of_colors[0])
#     list_of_colors . pop(0)
#     print("the list of the different colors name after removing the frist color name is : "+str(list_of_colors))
#     print("the length of the list of the different colors name after removing the frist color name is = "+str(len(list_of_colors))+" colors")
# get_lista_of_different_colors_name(lista_of_different_colors)

def get_lista_of_different_colors_name(list_of_colors) :
    print("the list of the different colors name before removing the frist color name is : "+str(list_of_colors))
    print("the length of the list of the different colors before removing the frist color name is = "+str(len(list_of_colors))+" colors")
    # list_of_colors . remove(list_of_colors[0])
    list_of_colors . pop(0)
    print("the list of the different colors name after removing the frist color name is : "+str(list_of_colors))
    return("the length of the list of the different colors name after removing the frist color name is = "+str(len(list_of_colors))+" colors")
lista_of_different_colors = []
# for i in range(5) :
    # lista_of_different_colors . append(input("please enter the different colors name to store in the list of the different colors name is : "))
lista_of_different_colors = [input("please enter the different colors name to store in the list of the different colors name to store in the list of the different colors name is : ") for i in range(5)]
colors = get_lista_of_different_colors_name(lista_of_different_colors)
print(colors)
