## write a python program to get the dictionary to get the total length of all values of a dictionary with string values =>
dictionary = {"color1": "red", "color2": "green" , "color3":"blue" , "color4": "navy", "color5":"teal" , "color6": "tomato"}
print("The Dictionary Is = ",str(dictionary))
length_of_values = 0
for i in dictionary.values():
    length_of_values += len(i) 
print("The Length Of The Total Values Is = ",str(length_of_values)," Characters")