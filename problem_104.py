# write a python program to get five colors name from the user in list , display that list of colors name , remove last color name , and then display all colors name for the user by using different functions methods =>
# lista_of_different_colors = []
# # for i in range(5) :
#     # lista_of_different_colors . append(input("please enter the different colors to store in the list of the colors is : "))
# lista_of_different_colors = [input("please enter the different colors name to store in the list of the different colors name is : ") for i in range(5)]
# def get_lista_of_colors(list_of_colors) :
#     print("the list of the different colors name before removing the last color name is : "+str(list_of_colors))
#     print("the length of the list of the different colors name before removing the last color name is : "+str(len(list_of_colors))+" colors")
#     # list_of_colors . pop()
#     # list_of_colors . pop(-1)
#     # list_of_colors . pop(4)
#     # list_of_colors . remove(list_of_colors[-1])
#     list_of_colors . remove(list_of_colors[4])
#     print("the list of the different colors name after removing the last color name is "+str(list_of_colors))
#     print("the length of the list of the different colors name after removing the last color name is = "+str(len(list_of_colors))+" colors")
# get_lista_of_colors(lista_of_different_colors)

def get_lista_of_colors(list_of_colors) :
    print("the list of the different colors name before removing the last color name is : "+str(list_of_colors))
    print("the length of the list of the different colors name before removing the last color name is = "+str(len(list_of_colors))+" colors")
    # list_of_colors . remove(list_of_colors[-1])
    # list_of_colors . remove(list_of_colors[4])
    # list_of_colors . pop()
    # list_of_colors . pop(-1)
    list_of_colors . pop(4)
    print("the list of the different colors name after removing the last color name is : "+str(list_of_colors))
    return("the length of the list of the different colors name after removing the last color name is = "+str(len(list_of_colors))+" colors")
lista_of_different_colors = []
# for i in range(5) :
    # lista_of_different_colors . append(input("please enter the different colors to store in the list of the different colors name is : "))
lista_of_different_colors = [input("please enter the different colors name to store in the list of the different colors name is : ") for i in range(5)]
colors = get_lista_of_colors(lista_of_different_colors)
print(colors)