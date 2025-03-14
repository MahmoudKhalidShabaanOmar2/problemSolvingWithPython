# write a python program to program to get the area , and parameter of the square , and find the sum of the both area , and parameter of the square , and then find square root of both area , and parameter of the square , and at the end find the sum of the square root of the area , and parameter of the square =>
# import math 
# length_of_square = int(input("please enter the length of the square is = "))
# print("the length of the square is = "+str(length_of_square))
# # area_of_square = length_of_square * length_of_square 
# # area_of_square = pow(length_of_square , 2)
# area_of_square = length_of_square ** 2
# print("the area of the square is = "+str(area_of_square))
# parameter_of_square = length_of_square * 4 
# print("the parameter of the square is = "+str(parameter_of_square))
# sum_of_parameter_area_of_square = length_of_square + parameter_of_square 
# print("the sum of the area of the square , and the parameter of the square is = "+str(sum_of_parameter_area_of_square))
# square_root_of_area_of_square = math . sqrt(area_of_square)
# print("the square root of the area of the square is = "+str(square_root_of_area_of_square))
# square_root_of_parameter_of_square = math . sqrt(parameter_of_square)
# print("the square root of the parameter of the square is = "+str(square_root_of_parameter_of_square))
# sum_of_square_root_of_area_parameter_of_square = square_root_of_area_of_square + square_root_of_parameter_of_square 
# print("the sum of the square root of the area of the square , and square root of the parameter of the square is = "+str(sum_of_square_root_of_area_parameter_of_square))

import math 
length_of_square = int(input("please enter the length of the square is = "))
print("the length of the square is = "+str(length_of_square))
if(length_of_square > 0) :
    # area_of_square = length_of_square * length_of_square 
    # area_of_square = pow(length_of_square , 2)
    area_of_square = length_of_square ** 2
    print("the area of the square is = "+str(area_of_square))
    parameter_of_square = length_of_square * 4
    print("the parameter of the square is = "+str(parameter_of_square))
    sum_of_area_parameter_of_square = area_of_square + parameter_of_square
    print("the sum of the area of the square , and the parameter of the square is = "+str(sum_of_area_parameter_of_square))
    square_root_of_area_of_square = math . sqrt(area_of_square)
    print("the square root of the area of the square is = "+str(square_root_of_area_of_square))
    square_root_of_parameter_of_square = math . sqrt(parameter_of_square)
    print("the square root of the parameter of the square is = "+str(square_root_of_parameter_of_square))
    sum_of_square_root_of_area_parameter_of_square = square_root_of_area_of_square + square_root_of_parameter_of_square 
    print("the sum of the square root of the area of the square , and the square root of the parameter of the square is = "+str(sum_of_square_root_of_area_parameter_of_square))
else :
    print("please enter a valid length of the square to get area , parameter , square root of area , and square root of parameter of the square")