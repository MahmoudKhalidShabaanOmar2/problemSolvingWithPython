# write a python program to get the total length of all values from the dictionary by using function method =>
dictionary = {"color1": "red", "color2": "green" , "color3":"blue" , "color4": "navy", "color5":"teal" , "color6": "tomato"}
def get_total_length_of_values_from_dictionary(dictio):
    print("The Dictionary Is : ",str(dictio))
    length_of_values = 0
    for i in dictio.values():
        length_of_values += len(i)
    print("The Length Of The Values From The Dictionary Is = ",str(length_of_values))
get_total_length_of_values_from_dictionary(dictionary)