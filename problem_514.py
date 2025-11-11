# write a python program to get the dictionary , and then store all keys into the tuple , and all values into the tuple by using function method =>
dictionary = {"color1": "red", "color2": "green" , "color3":"blue" , "color4": "navy", "color5":"teal" , "color6": "tomato"}
def get_tuple_of_keys_and_values_from_dictionary(dictio):
    print("The Dictionary Is : ",str(dictio))
    lista_of_keys = []
    for key in dictio.keys():
        lista_of_keys.append(key)
    print("The List Of All Keys From The Dictionary Is : ",str(lista_of_keys))
    tuple_of_keys = tuple(lista_of_keys)
    print("The Tuple Of All Keys From The Dictionary Is : ",str(tuple_of_keys))
    lista_of_values = []
    for value in dictio.values():
        lista_of_values.append(value)
    print("The List Of All Values From The Dictionary Is : ",str(lista_of_values))
    tuple_of_values = tuple(lista_of_values)
    print("The Tuple Of All Values From The Dictionary Is : ",str(tuple_of_values))
get_tuple_of_keys_and_values_from_dictionary(dictionary)