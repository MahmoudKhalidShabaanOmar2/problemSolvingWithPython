# write a python program to filter divisible by three number from the given dictionary keys , and then display only those values which have divisible by three numbers by using function method =>
dictionary = {1: "red", 2: "green" , 3:"blue" , 4: "navy", 5:"teal" , 6: "tomato"}
def access_divisible_by_three_keys_with_values_from_dictionary(dictio):
    print("The Dictionary Is : ",str(dictio))
    for key,value in dictio.items():
        if(key %3 == 0):
            print("The Key Is = ",str(key)," , And The Value Is : ",str(value))
access_divisible_by_three_keys_with_values_from_dictionary(dictionary)