# write a python program to get ten colors to store in the list of colors , then displaying the list of colors , displaying the copied , Or cloned of list of colors , and at the end remove the last color from the list of colors by using function method =>
# lista_of_colors = []
# for i in range(10) :
#     colors = input(f"Please Enter Color {i + 1} Is : ")
#     lista_of_colors . append(colors)
# def get_lista_of_colors(list_of_colors) :
#     print("The List Of The Colors Is : "+str(list_of_colors))
#     for i in list_of_colors :
#         print(i)
#     list_of_colors . pop()
#     print("The List Of The Colors After Removing The Last Color From The List Of The Color Is : "+str(list_of_colors))
#     # copied_list_of_list_colors = list_of_colors[:]
#     # copied_list_of_list_colors = list(list_of_colors)
#     copied_list_of_list_colors = list_of_colors . copy()
#     print("The Copied List Of The Colors Is : "+str(copied_list_of_list_colors))
# get_lista_of_colors(lista_of_colors)

def get_lista_of_colors(list_of_colors) :
    print("The List Of The Colors Is : "+str(list_of_colors))
    for i in list_of_colors :
        print(i)
    # list_of_colors.pop()
    # list_of_colors.pop(-1)
    list_of_colors.pop(9)
    print("The List Of The Colors After Removing The Last Color From The List Of The Colors Is : "+str(list_of_colors))
    # copied_list_of_colors = list_of_colors.copy()
    # copied_list_of_colors = list_of_colors[:]
    copied_list_of_colors = list(list_of_colors)
    return("The Copied , Or Cloned List Of Colors Is : "+str(copied_list_of_colors))
lista_of_colors = []
for i in range(10) :
    colors = input(f"Please Enter The Color {i + 1} Is : ")
    lista_of_colors.append(colors)
displaying_list_of_colors = get_lista_of_colors(lista_of_colors)
print(displaying_list_of_colors)

    