# write a python program to get shuffle code of a list of colors =>
import random 
lista_of_colors_codes = []
for i in range(5) :
    lista_of_colors_codes.append(input("Please enter the colors codes to store in the list of the different colors is : "))
print("The List Of The Different Colors Is : ",str(lista_of_colors_codes))
random . shuffle(lista_of_colors_codes)
print(lista_of_colors_codes)