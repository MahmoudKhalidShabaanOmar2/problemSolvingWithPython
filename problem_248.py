# write a python program to get a shuffle of list of different colors codes by using functions methods =>
# import random 
# lista_of_different_colors_codes = []
# # for i in range(5) :
# #     colors_codes = input("please enter different colors codes to store in the list of the different colors codes is : ")
# #     lista_of_different_colors_codes.append(colors_codes)
# lista_of_different_colors_codes = [input("please enter the different colors codes to store in the list of the different colors codes is : ") for i in range(5)]
# def get_different_colors_codes(list_of_colors_codes) :
#     print("the list of the different colors codes is : "+str(list_of_colors_codes))
#     random . shuffle(list_of_colors_codes)
#     print("The list of the different colors codes after shuffeling is : "+str(list_of_colors_codes))
# get_different_colors_codes(lista_of_different_colors_codes)

import random 
def get_lista_of_different_colors_codes(list_of_colors_codes) :
    print("the list of the different colors codes is : "+str(list_of_colors_codes))
    random.shuffle(list_of_colors_codes)
    return("the list of the different colors codes after shuffleing is : "+str(list_of_colors_codes))
lista_of_different_colors_codes = []
for i in range(5) :
    colors_codes = input("please enter the different colors codes to store in the list of the different colors codes is : ")
    lista_of_different_colors_codes.append(colors_codes)
different_colors_codes = get_lista_of_different_colors_codes(lista_of_different_colors_codes)
print(different_colors_codes)