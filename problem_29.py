# write a python program to get number from the user and then get table of this number =>
number = int(input("please enter the number is = "))
print("the number is = "+str(number))
print("generating table of the number is : \n")
for num in range(1 , 11) :
    print(str(num)+" * "+str(number)+" = "+str(num * number))