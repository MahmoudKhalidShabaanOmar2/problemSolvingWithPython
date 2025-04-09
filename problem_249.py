# write a python program to get a shuffle of the list of the different colors codes in ascending order , and descending order by using different functions methods =>
import random 
lista_of_different_colors_codes = []
for i in range(5) :
    lista_of_different_colors_codes . append(input("please enter the different colors codes to store in the list of the different colors codes is : "))
def get_lista_of_different_colors_codes(list_of_colors_codes) :
    print("the list of the different colors codes in the ascending order is : "+str(list_of_colors_codes))
    for j in list_of_colors_codes:
        print(j)
    random . shuffle(list_of_colors_codes)
    print("the list of the different colors codes after shuffling in the ascending order is : "+str(lista_of_different_colors_codes))
    for k in list_of_colors_codes :
        print(k)
    # list_of_colors_codes.reverse()
    
    print("the list of the different colors codes after shuffling in the descending order is : "+str(list_of_colors_codes))
    for l in list_of_colors_codes :
        print(l)
get_lista_of_different_colors_codes(lista_of_different_colors_codes)