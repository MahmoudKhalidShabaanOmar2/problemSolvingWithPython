# write a python program to get the dictionary , and then store all keys , and values from the dictionary into two tuples =>
dictionary = {"color1": "red", "color2": "green" , "color3":"blue" , "color4": "navy", "color5":"teal" , "color6": "tomato"}
print("The Dictionary Is : ",str(dictionary))
lista_of_keys = []
for i in dictionary.keys():
    lista_of_keys.append(i)
print("The List Of Keys Is : ",str(lista_of_keys))
tuple_of_keys = tuple(lista_of_keys)
print("The Tuple Of All Keys Is : ",str(tuple_of_keys))
lista_of_values = []
for j in dictionary.values():
    lista_of_values.append(j)
print("The List Of Values Is : ",str(lista_of_values))
tuple_of_values = tuple(lista_of_values)
print("The Tuple Of Values Is : ",str(tuple_of_values))