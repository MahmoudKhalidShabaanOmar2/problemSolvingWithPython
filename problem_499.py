# write a python program to filter odd numbers from a given dictionary keys , and then displaying only those values that have odd keys by using function method =>
dicionary = {1: "Ahmed", 2: "Mahmoud" , 3: "Mohamed" , 4: "Khalid" , 5: "Hussien" , 6: "Hassan"}
def access_odd_keys_with_values_from_dictionary(dictio):
    print("The Dictionary Is : ",str(dictio))
    for key,value in dictio.items():
        if(key %2 != 0):
            print("The Key Is : ",str(key)," And The Value Is : ",str(value))
access_odd_keys_with_values_from_dictionary(dicionary)