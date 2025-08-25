# write a python program to update the specific keys in the dectionary by using function method =>
dictionary_of_user_information = {"name" : "Mahmoud Khalid Shabaan" , "age" : "22 Years" , "faculty" : "Computer Science , And Information System"}
print("The Dictionary Of The User Information Is : ",str(dictionary_of_user_information))
old_key = input("Please Enter The Old Key Is : ")
print("The Old Key Is : ",old_key)
new_key = input("Please Enter The New Key Is : ")
print("The New Key Is : ",new_key)
dictionary_of_user_information[new_key] = dictionary_of_user_information[old_key]
del dictionary_of_user_information[old_key]
print("The Dictionary Of The User Information After Updating The Specific Key Is : ",str(dictionary_of_user_information))