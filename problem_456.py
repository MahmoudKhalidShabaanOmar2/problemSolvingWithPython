# write a python program to sort dictionary by keys , and get the dictionary from the user =>
numbers_of_terms = int(input("Please Enter The Number Of The Terms Is = "))
print("The Number Of The Terms Is = ",str(numbers_of_terms)," Terms")
dictionary_of_user_information = {}
for i in range(numbers_of_terms):
    dictionary_key = input(f"Please Enter The Dictionary Key ({i + 1}) Is : ")
    dictionary_value = input(f"Please Enter The Dictionary Value ({i + 1}) Is : ")
    dictionary_of_user_information[dictionary_key] = dictionary_value 
print("The Dictionary of The User Information Is : ",str(dictionary_of_user_information))
sorted_of_dictionary_of_user_information_by_keys = dict(sorted(dictionary_of_user_information.items()))
print("The Sorted Of The Dictionary Of The User Information By Keys Is : ",str(sorted_of_dictionary_of_user_information_by_keys))