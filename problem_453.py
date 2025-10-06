# write a python program to get a dictionary , and then updated the specific key from the dictionary on the running time process =>
dictionary_of_user_information = {"name" : "Mahmoud Khalid" , "age" : "23 Years Old" , "gender" : "Male"}
print("The Original Dictionary Of The User Information Is : ",str(dictionary_of_user_information))
old_key = input("Please Enter The Old Key Is : ")
print("The Old Key Is : ",old_key)
new_key = input("Please Enter The New Key Is : ")
print("The New Key Is : ",new_key)
dictionary_of_user_information[new_key] = dictionary_of_user_information[old_key]
del dictionary_of_user_information[old_key]
print("The Updated Dictionary Of The User Information Is : ",str(dictionary_of_user_information))