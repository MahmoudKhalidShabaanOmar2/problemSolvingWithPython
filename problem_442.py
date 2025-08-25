# write a python program to get the dictionary of the user information from the user , and then sorted the dictionary by using values by using function method =>
dictionary_of_user_information = {"name" : "Mahmoud" , "age" : "22 years" , "gender" : "male" , "jobTitle" : "Frontend"}
print("The Dictionary Of The User Information Is : ",str(dictionary_of_user_information))
new_dictionary_of_user_information = sorted(dictionary_of_user_information.items() , key=lambda  item:item[1])
print("The Updated Dictionary Of The User Information Is : ",str(new_dictionary_of_user_information))