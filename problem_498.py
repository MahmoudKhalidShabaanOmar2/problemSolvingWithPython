# write a python program to get the alphabetic string based dictionary to print items in the upper case by using function method =>
dictionary = {"a": "apple" , "b": "banana" , "p": "pine apple" , "w": "water melon"}
def access_keys_with_values_in_uppers_from_dictionary(dictio):
    print("The Dictionary Is : ",str(dictio))
    for key,value in dictio.items():
        print("The Key Is : ",str(key.upper())+" , And The Value Is : ",str(value.upper()))
access_keys_with_values_in_uppers_from_dictionary(dictionary)