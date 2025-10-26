# write a python program to filter even number from the given dictionary keys , and then display only those values which have even numbers by using fuction method =>
dictionary = {1: "Ahmed", 2: "Mohamed" , 3: "Khalid" , 4: "Omar" , 5: "Ziad", 6: "kamal"}
def access_even_keys_values_from_dictionary(dictio):
    print("The Dictionary Is : ",str(dictio))
    for key,value in dictio.items():
        if(key %2 == 0):
            print("The Key Is = ",str(key), " , And The Value Is : ",str(value))
access_even_keys_values_from_dictionary(dictionary)