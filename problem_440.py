# write a python program to get the dictionary of the user information from the user , and then get the length of the keys , and values inside the dictionary by using function method =>
dictionary_of_user_information = {"name" : "Mahmoud Khalid Shabaan Omar" , "age" : "22 Years" , "faculty" : "Computer Science , And Information System"}
def get_length_of_keys_values_Of_dictionary_of_user_information(dict_of_user_info):
    print("The Dicitionsry Of The User Information Is : ",str(dict_of_user_info))
    length_dictionary_of_user_information = len(dict_of_user_info)
    print("The Length Of The Dictionary Of The User Information Is = ",str(length_dictionary_of_user_information))
    length_of_keys_inside_dictionary_of_user_information = len(dict_of_user_info.keys())
    print("The Length Of The Keys Inside The Dictionary Of The User Information Is = ",str(length_of_keys_inside_dictionary_of_user_information)," Keys")
    length_of_values_inside_dictionary_of_user_information = len(dict_of_user_info.values())
    print("The Length Of The Values Inside The Dictionary Of The User Information Is = ",str(length_of_values_inside_dictionary_of_user_information)+" Values")
get_length_of_keys_values_Of_dictionary_of_user_information(dictionary_of_user_information)