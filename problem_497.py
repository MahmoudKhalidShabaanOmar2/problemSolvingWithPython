# write a python program to print a dictionary items line by line , key and value should have one tab distance by using function method =>
dictionary = {1: "Red" , 2: "Blue" , 3: "Green" , 4: "Yellow"}
def access_keys_values_from_dictionary(dictio):
    print("The Dictionary Is : ",str(dictio))
    for key,value in dictio.items():
        print("The Key Is = ",str(key),"\t , And The Value Is : ",str(value))
access_keys_values_from_dictionary(dictionary)