# write a python program to get ten colors in a list , and then get the copied , or cloned of the list of the colors by using function methods :  
# lista_of_colors = []
# for i in range(10) :
#     colors = input(f"Please Enter Color {i + 1} Is : ")
#     lista_of_colors.append(colors)
# def get_lista_of_colors(list_of_colors) :
#     print("The List Of Colors Is : "+str(list_of_colors))
#     for i in list_of_colors :
#         print(i)
#     # copied_of_list_of_colors = list_of_colors[:]
#     # copied_of_list_of_colors = list_of_colors . copy()
#     copied_of_list_of_colors = list(list_of_colors)
#     print("The Copied , Or Cloned List Of Colors Is : "+str(copied_of_list_of_colors))
# get_lista_of_colors(lista_of_colors)

def get_lista_of_colors(list_of_colors) :
    print("The List Of The Colors Is : "+str(list_of_colors))
    for i in list_of_colors : 
        print(i)
    # copied_list_of_colors = list_of_colors[:]
    # copied_list_of_colors = list(list_of_colors)
    copied_list_of_colors = list_of_colors.copy()
    return("The Copied , Or Cloned List Of Colors Is : "+str(copied_list_of_colors))
lista_of_colors = []
for j in range(10) :
    colors = input(f"Please Enter The Color {j + 1} Is : ")
    lista_of_colors.append(colors)
displaying_list_of_colors = get_lista_of_colors(lista_of_colors)
print(displaying_list_of_colors)