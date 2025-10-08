# write a python program to get the dictionary of user information , and then sorted the dictionary by specific keys by using function method =>
dictionary_of_user_information = {"name" : "Mahmoud Khalid" , "age" : "23 Years Old" , "gender" : "male" , "faculty" : "Computer Science"}
def sorted_dictionary_by_using_specific_key(dict_of_user_info):
    print("The Dictionary Of The User Information Is : ",str(dict_of_user_info))
    sorted_dictionary_of_user_information_by_keys = dict(sorted(dict_of_user_info.items()))
    print("The Sorted Dictionary Of The User Information By Using Specific Keys Is : ",str(sorted_dictionary_of_user_information_by_keys))
sorted_dictionary_by_using_specific_key(dictionary_of_user_information)