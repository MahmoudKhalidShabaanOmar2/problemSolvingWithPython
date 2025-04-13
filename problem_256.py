# write a python program to get ten colors from the user in a list , and then get the copied , or cloned of the list , and at the end remove , or delete the last color from the list of the colors =>
lista_of_colors = []
for i in range(10) :
    colors = input("Please Enter The Colors To Store In The List Of The Colors Is : ")
    lista_of_colors.append(colors) 
print("The List Of The Colors Is : "+str(lista_of_colors))
copied_lista_of_colors = lista_of_colors[:]
print("The Copied , Or Cloned List Of The Colors Is : "+str(copied_lista_of_colors)) 
copied_lista_of_colors.pop() 
print("The Copied , Or Cloned List Of The Colors After Removing The Last Color Is : "+str(copied_lista_of_colors))