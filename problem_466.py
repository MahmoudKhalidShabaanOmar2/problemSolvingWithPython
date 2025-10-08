# write a python program to get dictionary of user inforrmation , and then sorted the dictionary of the user information by values by using function method =>
dictionary_of_user_information = {"name" : "Mahmoud" , "gender" : "Male" , "faculty" : "Computer Science" , "jobTitle" : "Frontend"}
def sorted_dictionary_of_user_information_by_values(dict_of_user_info):
    print("The Dictionary Of The User Information Is : ",str(dict_of_user_info))
    sorted_of_dictionary_of_user_information_by_values = dict(sorted(dictionary_of_user_information.items() , key=lambda item:item[1]))
    print("The Sorted Of The Dictionary Of The User Information By Values Is : ",str(sorted_of_dictionary_of_user_information_by_values))
sorted_dictionary_of_user_information_by_values(dictionary_of_user_information)