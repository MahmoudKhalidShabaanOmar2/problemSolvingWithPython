# write a python program to get the suhffle of the list of the different colors in descending order , and ascending order =>
import random 
lista_of_different_colors = []
for i in range(5) : 
    lista_of_different_colors . append(input("please enter different colors codes to store in the list of the different colors codes is : "))
random . shuffle(lista_of_different_colors)
print("the list of the different colors codes in the ascending order is : "+str(lista_of_different_colors))
for j in lista_of_different_colors : 
    print(j)
lista_of_different_colors . sort(reverse = True) 
print("the list of the different colors codes in the descending order is : "+str(lista_of_different_colors))
for k in lista_of_different_colors :
    print(k)