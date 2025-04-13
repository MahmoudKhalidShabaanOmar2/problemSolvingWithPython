# write a python program to get a ten colors in a list , and then get clone , or copy of the list of colors =>
lista_of_colors = []
for i in range(10) :
    colors = input("Please Enter Colors To Store In The List Of The Colors Is : ")
    lista_of_colors . append(colors)
print("The List Of The Colors Is : "+str(lista_of_colors))
# copied_lista_of_colors = lista_of_colors . copy()
# copied_lista_of_colors = list(lista_of_colors)
copied_lista_of_colors = lista_of_colors[:]
print("The Copied , Or Cloned List Of The Colors Is : "+str(copied_lista_of_colors))