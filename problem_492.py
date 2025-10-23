# write a python program to print a dictionary items line by line , key and value should have one tab distance =>
dictionary = {1: "Red" , 2: "blue" , 3: "black" , 4: "green"}
print("The Dictionary Is : ",str(dictionary))
for k,v in dictionary.items():
    print("the Key Is = ",str(k)+"\t"," The Value Is : ",str(v))