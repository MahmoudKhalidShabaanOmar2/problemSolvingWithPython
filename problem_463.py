# write a python program to get the dictionary of user information , and then get the total numbers of keys , and values in the dictionary of user information by using function method =>
dictionary_of_user_information = {"name" : "Mahmoud Khalid" , "age" : "23 Years Old" , "gender" : "Male"}
def get_total_numbers_of_keys_and_values(dict_of_user_info):
    print("The Dictionary Of The User Information Is : ",str(dict_of_user_info))
    total_numbers_of_keys = len(dict_of_user_info.keys())
    print("The Total Numbers Of The Keys Inside The Dictionary of The User Information Is = ",str(total_numbers_of_keys)," Keys")
    total_numbers_of_Values = len(dict_of_user_info.values())
    print("The Total Numbers Of Values Inside The Dictionary Of The User Information Is : ",str(total_numbers_of_Values)," Values")
get_total_numbers_of_keys_and_values(dictionary_of_user_information)