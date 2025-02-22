# write a python program to get a number from the user , and then get cube of the number by using different function methods =>
# number = int(input("please enter the number is = "))
# def get_cube_of_num(num) :
#     print("the number is = "+str(num))
#     # cube_of_num = num * num * num 
#     # cube_of_num = num ** 3
#     cube_of_num = pow(num , 3)
#     print("the cube of the number is = "+str(cube_of_num))
# get_cube_of_num(number)

def get_cube_of_num(num) :
    print("the number is = "+str(num))
    # cube_of_num = num * num * num 
    # cube_of_num = pow(num , 3)
    cube_of_num = num ** 3
    return("the cube of the number is = "+str(cube_of_num))
number = int(input("please enter the number is = "))
cube = get_cube_of_num(number)
print(cube)