# write a python program to filter divisible by three number from the given dictionary keys , and then display only those values which have divisible by three numbers =>
dictionary = {1: "Ahmed", 2: "Mohamed" , 3: "Khalid" , 4: "Youssef" , 5: "Ziad" , 6: "Mazen"}
print("The Dictionary Is : ",str(dictionary))
for key,value in dictionary.items():
    if(key %3 == 0):
        print("The Key Is = ",str(key)," , And The Value Is : ",str(value))