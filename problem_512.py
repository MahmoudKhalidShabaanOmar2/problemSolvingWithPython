# write a python program to get the dictionary from the user , and then store all keys in a list of keys , and store all values in a list of values from the dictionary by using function method =>
def store_keys_values_into_two_lists_from_dictionary(dictio):
    print("The Dictionary Is : ",str(dictio))
    lista_of_keys = []
    for i in dictio.keys():
        lista_of_keys.append(i)
    print("The List Of Keys Is : ",str(lista_of_keys))
    lista_of_values = []
    for j in dictio.values():
        lista_of_values.append(j)
    return "The List Of Values Is : "+str(lista_of_values)
dictionary = {"color1": "red", "color2": "green" , "color3":"blue" , "color4": "navy", "color5":"teal" , "color6": "tomato"}
displaying = store_keys_values_into_two_lists_from_dictionary(dictionary)
print(displaying)