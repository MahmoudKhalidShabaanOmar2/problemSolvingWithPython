# write a python program to get number from the user and then get the cube of the number =>
num = int(input("please enter the number is = "))
print("the number is = \""+str(num)+"\"")
# cube_of_num = num * num * num 
# cube_of_num = num ** 3
cube_of_num = pow(num , 3)
print("the cube of the number is = \""+str(cube_of_num)+"\"")