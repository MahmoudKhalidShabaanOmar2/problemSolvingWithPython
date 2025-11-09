# write a python program to get the total length of all keys , and values from the dictionary , and then displaying the sum of the length of keys , and values =>
dictionary = {"color1": "red", "color2": "green" , "color3":"blue" , "color4": "navy", "color5":"teal" , "color6": "tomato"}
print("The Dictionary Is : ",str(dictionary))
length_of_keys = 0
length_of_values = 0
for i in dictionary.keys():
    length_of_keys += len(i)
print("The Length Of The Keys Is = ",str(length_of_keys)," Characters")
for j in dictionary.values():
    length_of_values += len(j)
print("The Length Of The Values Is = ",str(length_of_values)," Characters")
print("The Sum Of The Length Of Keys , And Length Of Values Is = ",str(length_of_keys + length_of_values)+" Characters")