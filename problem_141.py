# write a python program to get starting number , and ending number from the user as input , and then generate all numbers in the properly sequence =>
starting_num = int(input("please enter the starting number is = "))
ending_num = int(input("please enter the ending number is = "))
print("the starting number is = \" "+str(starting_num)+" \"")
print("the ending number is = \""+str(ending_num)+" \"")
print("generating all numbers from the starting number = \" "+str(starting_num)+" \" to the ending number is = \" "+str(ending_num)+" \" in the ascending(properly) sequence is : ")
for num in range(starting_num , ending_num + 1) :
    print(num) 