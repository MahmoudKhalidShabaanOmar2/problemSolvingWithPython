# write a python program to create a alpha string based dictionary to print dictionary items in uppercase:
dictionary = {"a":"apple" , "b" : "peach" , "c" : "water melon" , "d" : "pine apple"}
print("The Dictionary Is : ",str(dictionary))
for k,v in dictionary.items():
    print("The Key Is : ",str(k.upper())," , And The Value Is : ",str(v.upper()))