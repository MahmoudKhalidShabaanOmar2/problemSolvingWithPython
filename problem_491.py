# write a python program to get the nested dictionary , and then access value from the nested dictionary by using function method =>
nested_dictionary = {1: {"name": "Mahmoud Khalid"} , 2 : {"color" : "Light Sky"}, 3 : {"age" : "23 Years Old"}}
def access_Values_from_nested_dictionary(nested_dict):
    print("The Nested Dictionary Is : ",str(nested_dict))
    print("The Name From The Nested Dictionary Is : ",str(nested_dict[1]["name"]))
    print("The Color From The Nested Dictionary Is : ",str(nested_dict[2]["color"]))
    print("The Age Fom The Nested Dictionary Is : ",str(nested_dict[3]["age"]))
access_Values_from_nested_dictionary(nested_dictionary)