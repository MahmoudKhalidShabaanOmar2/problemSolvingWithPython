# write a python program to filter even number from the given dictionary keys , and then display only those values which have even numbers =>
dictionary = {1: "ahmed" , 2 : "mohamed" , 3 : "khalid" , 4 : "tarek" , 5 : "ziad" , 6 : "jana"}
print("The Dictionary Is : ",str(dictionary))
for k,v in dictionary.items():
    if(k %2 == 0):
        print("The Key Is = ",str(k)," , And The Value Is : ",str(v))