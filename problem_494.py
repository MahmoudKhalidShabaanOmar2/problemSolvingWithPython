# write a python program to filter odd numbers from a given dictionary keys , and then displaying only those values that have odd keys =>
dictionary = {1 : "ahmed" , 2 : "mohamed" , 3 : "khalid" , 4 : "tarek" , 5 : "omar" , 6 : "amr"}
print("The Dictionary Is : ",str(dictionary))
for k,v in dictionary.items():
    if(k %2 != 0):
        print("The Key Is = ",str(k)," The Value Is : ",str(v))