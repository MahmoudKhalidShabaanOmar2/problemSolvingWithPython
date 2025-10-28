# write a python program to filter divisible by three number from the given dictionary keys , and then display only those values which have divisible by five numbers =>
dictionary = {1: "red", 2: "green" , 3:"blue" , 4: "navy", 5:"teal" , 6: "tomato"}
for key,value in dictionary.items():
    if(key %5 == 0):
        print("The Key Is ",str(key), " , And The Value Is : ",str(value))