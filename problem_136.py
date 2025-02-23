# write a python program to get angle from the user , and find it's sin , and cos value in radian , and then converted their results into degree unit by using different functions methods =>
# import math 
# angle = float(input("please enter the angle is = "))
# def get_sin_cos_into_radian_converted_to_degree(ang) :
#     print("the angle is = "+str(ang)+" rad")
#     cos_value_in_radian = math . cos(ang)
#     print("the cos value in the radian  is = "+str(cos_value_in_radian)+" rad")
#     cos_value_in_degree = math . degrees(cos_value_in_radian)
#     print("the cos value in the degree  is = "+str(cos_value_in_degree)+" deg")
#     sin_value_in_radian = math . sin(angle) 
#     print("the sin value in the radian  is = "+str(sin_value_in_radian)+" rad")
#     sin_value_in_degree = math . degrees(sin_value_in_radian)
#     print("the sin value in the degree is = "+str(sin_value_in_degree)+" deg")
# get_sin_cos_into_radian_converted_to_degree(angle)

import math 
def get_sin_cos_into_radian_converted_to_degree(ang) :
    print("the angle is = "+str(ang)+" rad")
    sin_value_in_radian = math . sin(ang)
    print("the sin value in the radian is = "+str(sin_value_in_radian)+" rad")
    sin_value_in_degree = math . degrees(sin_value_in_radian)
    print("the sin value in the degree is = "+str(sin_value_in_degree)+" deg")
    cos_value_in_radian = math . cos(ang)
    print("the cos value in the radian is = "+str(cos_value_in_radian)+" rad")
    cos_value_in_degree = math . degrees(cos_value_in_radian)
    return("the cos value in the degree is = "+str(cos_value_in_degree)+" deg")
angle = float(input("please enter the angle is = "))
sin_cos = get_sin_cos_into_radian_converted_to_degree(angle)
print(sin_cos)