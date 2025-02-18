# write a python program to get number from the user , and then get the cube of the number by using function methods =>
# number = int(input("please enter the number is = "))
# print("the number is = "+str(number))
# # cube_of_number = number * number * number 
# # cube_of_number = number ** 3
# cube_of_number = pow(number , 3)
# def get_cube_of_num(number , cube_of_num) :
#     print("the number is = "+str(number))
#     print("the cube of the number is = "+str(cube_of_num))
# get_cube_of_num(number , cube_of_number)

# number = int(input("please enter the number is = "))
# def get_cube_of_num(num) :
#     print("the number is = "+str(num))
#     if(num > 0) :
#         # cube_of_num = num * num * num
#         # cube_of_num = num ** 3
#         cube_of_num = pow(num , 3)
#         print("the cube of the number is = "+str(cube_of_num))
#     elif(num <= 0) :
#         print("there is no cube of the number , because your entered number is = "+str(num))
#     else :
#         print("please enter valid number")
# get_cube_of_num(number)

# def get_cube_of_num(num) :
#     print("the number is = "+str(num))
#     # cube_of_num = num * num * num 
#     # cube_of_num = num ** 3
#     cube_of_num = pow(num , 3)
#     return("the cube of the number is = "+str(cube_of_num))
# number = int(input("please enter the number is = "))
# cube_of_number = get_cube_of_num(number)
# print(cube_of_number)

def get_cube_of_num(num) :
    print("the number is = "+str(num))
    if(num > 0) :
        # cube_of_num = num * num * num 
        # cube_of_num = num ** 3
        cube_of_num = pow(num , 3)
        return("the cube of the number is = "+str(cube_of_num))
    else :
        return("there is no cube of the number , because your entered number is = "+str(num))
number = int(input("please enter the number is = "))
cube_of_number = get_cube_of_num(number)
print(cube_of_number)