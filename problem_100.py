# write a python program to get colors name from the user in the list , and then store in the list , and count the list , and then display the result for the user by using functions methods=>
# lista_of_colors = ["red" , "green" , "blue" , "yellow" , "orange" , "pink" , "teal" , "tomato" , "darkblue" , "black"]
# def get_lista_of_colors_and_count_colors(list_of_colors) :
#     print("the list of the colors is : "+str(list_of_colors))
#     print("the length of the list of the different colors name is = "+str(len(list_of_colors))+" colors")
# get_lista_of_colors_and_count_colors(lista_of_colors)

def get_lista_of_colors_and_count_colors(list_of_colors) :
    print("the list of the colors is : "+str(list_of_colors))
    return("the length of the list of the different colors name is = "+str(len(list_of_colors))+" colors")
lista_of_colors = ["red" , "green" , "blue" , "yellow" , "orange" , "pink" , "teal" , "tomato" , "darkblue" , "black"]
colors = get_lista_of_colors_and_count_colors(lista_of_colors)
print(colors)