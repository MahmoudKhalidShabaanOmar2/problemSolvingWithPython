# write a python program to get the dictionary , and then store all keys from the dictionary into the list , and then store all values from the dictionary in another key =>
dictionary = {"color1": "red", "color2": "green" , "color3":"blue" , "color4": "navy", "color5":"teal" , "color6": "tomato"}
print("The Dictionary Is : ",str(dictionary))
lista_of_keys = []
for key in dictionary.keys():
    lista_of_keys.append(key)
print("The List Of All Keys Is : ",str(lista_of_keys))
lista_of_values = []
for value in dictionary.values():
    lista_of_values.append(value)
print("The List Of All Values Is : ",str(lista_of_values))