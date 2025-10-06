# write a python program to get the dictionary of the user information from the user , anad then sorted the dictionary by values =>
numbers_of_terms = int(input("Please Enter The Numbers Of Terms Is = "))
print("The Number Of Terms Is = ",str(numbers_of_terms)," Terms")
dictionary_of_user_information = {}
for i in range(numbers_of_terms):
    dictionary_key = input(f"Please Enter The Dictionary Key({i + 1}) Is : ")
    dictionary_value = input(f"Please Enter The Dictionary Value({i + 1}) Is : ")
    dictionary_of_user_information[dictionary_key] = dictionary_value 
print("The Dictionary of The User Information Is : ",str(dictionary_of_user_information))
sorted_of_dictionary_of_user_information_by_values = dict(sorted(dictionary_of_user_information.items() , key=lambda item:item[1]))
print("The Sorted Of The Dictionary of The User Information By Values Is : ",str(sorted_of_dictionary_of_user_information_by_values))