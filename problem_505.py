# write a python program to get the dictionary to get the total length of all keys of a dictionary with string keys =>
dictionary = {"color1": "red", "color2": "green" , "color3":"blue" , "color4": "navy", "color5":"teal" , "color6": "tomato"}
print("The Dictionary Is : ",str(dictionary))
length_of_keys = 0
for i in dictionary.keys():
    length_of_keys += len(i)
print("The Length Of The Keys From The Dictionary Is = ",str(length_of_keys), " Keys")