# write a python program to get length of the square , get the area , and paramter of the square , and then get the sum of the area , and parameter of the square , and then get the square root of the area , and parameter of the square , and at the end get the sum of the square root of the area , and parameter of the square by using different functions methods =>
# import math 
# length_of_square = int(input("please enter the length of the square is = "))
# def get_area_parameter_of_square(len_of_sqr) :
#     print("the length of the square is = "+str(len_of_sqr))
#     area_of_square = len_of_sqr * len_of_sqr 
#     print("the area of the square is = "+str(area_of_square))
#     parameter_of_square = len_of_sqr * 4
#     print("the parameter of the square is = "+str(parameter_of_square))
#     sum_of_area_parameter_of_square = area_of_square + parameter_of_square 
#     print("the sum of the area of the square , and parameter of the square is = "+str(sum_of_area_parameter_of_square))
#     square_root_of_area_of_square = math . sqrt(area_of_square)
#     print("the square root of the area of the square is = "+str(square_root_of_area_of_square))
#     square_root_of_parameter_of_square = math . sqrt(parameter_of_square)
#     print("the square root of the parameter of the square is = "+str(square_root_of_parameter_of_square))
#     sum_of_square_root_of_area_parameter_of_square = square_root_of_area_of_square + square_root_of_parameter_of_square 
#     print("the sum of the square root of the area of the square , and the square root of the parameter of the square is = "+str(sum_of_square_root_of_area_parameter_of_square))
# get_area_parameter_of_square(length_of_square)

import math 
length_of_square = int(input("please enter the length of the square is = "))
def get_area_parameter_of_square(len_of_sqr) :
    print("the length of the square is = "+str(len_of_sqr))
    if(len_of_sqr > 0) :
        # area_of_square = len_of_sqr * len_of_sqr
        # area_of_square = pow(len_of_sqr , 2) 
        area_of_square = len_of_sqr ** 2 
        print("the area of the square is = "+str(area_of_square))
        parameter_of_square = len_of_sqr * 4
        print("the parameter of the square is = "+str(parameter_of_square))
        sum_of_area_parameter_of_square = area_of_square + parameter_of_square 
        print("the sum of the area of the square , and parameter of the square is = "+str(sum_of_area_parameter_of_square))
        square_root_of_area_of_square = math . sqrt(area_of_square)
        print("the square root of the area of the square is = "+str(square_root_of_area_of_square))
        square_root_of_parameter_of_square = math . sqrt(parameter_of_square)
        print("the square root of the parameter of the square is = "+str(square_root_of_parameter_of_square))
        sum_of_square_root_of_area_parameter_of_square = square_root_of_area_of_square + square_root_of_parameter_of_square 
        print("the sum of the square root of the area of the square , and square root of the parameter of the square is = "+str(sum_of_square_root_of_area_parameter_of_square))
    else :
        print("please enter a valid length of the square to get area , parameter , square root of area of square , and at the end square root of parameter of square")
get_area_parameter_of_square(length_of_square)