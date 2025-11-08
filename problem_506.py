# write a python program to get the dictionary to get the total length of all keys of a dictionary with string keys by using function =>
dictionary = {"color1": "red", "color2": "green" , "color3":"blue" , "color4": "navy", "color5":"teal" , "color6": "tomato"}
def get_legth_of_keys_from_dictionary(dictio):
    print("The Dictionary Is : ",str(dictio))
    length_of_keys = 0
    for i in dictio.keys():
        length_of_keys += len(i)
    print("The Length Of All Keys From The Dictionary Is = ",str(length_of_keys)," characters")
get_legth_of_keys_from_dictionary(dictionary)