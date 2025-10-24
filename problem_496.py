# write a python program to get the dictionary from the user ,  and then access values fom the dictionary by using function method =>
dictionary = {1: {"name" : "Mahoud Khalid"} , 2:{"age" : "23 Years Old"} , 3 :{"color": "Red"}}
def access_dictionary_values(dictio):
    print("The dictionary Is : ",str(dictionary))
    print("The Name from The Dictionary is : ",str(dictionary[1]["name"]))
    print("The Age Fro The Dictionary Is  ",str(dictionary[2]["age"]))
    print("The color From The Dictionary Is : ",str(dictionary[3]["color"]))
access_dictionary_values(dictionary)