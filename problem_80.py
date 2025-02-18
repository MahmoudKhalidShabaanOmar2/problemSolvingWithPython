# write a python program to get number from the user , and then get the cube of the number =>
# number = int(input("please enter the number is = "))
# print("the number is = "+str(number))
# # cube_of_number = number * number * number 
# # cube_of_number = number ** 3
# cube_of_number = pow(number , 3)
# print("the cube of the number is = "+str(cube_of_number))

number = int(input("please enter the number is = "))
print("the number is = "+str(number))
if(number > 0) :
    # cube_of_number = number * number * number 
    # cube_of_number = number ** 3
    cube_of_number = pow(number , 3)
    print("the cube of the number is = "+str(cube_of_number))
else :
    print("there is no cube of the number , because your entered number is = "+str(number))
