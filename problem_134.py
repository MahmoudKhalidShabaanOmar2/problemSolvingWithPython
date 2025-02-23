# write a python program to get angle from the user , and then get the cos , and sin value in the radian by using different functions methods =>
# import math 
# angle = float(input("please enter the angle is = "))
# def get_cos_and_sin_in_radian(ang) :
#     print("the angle is = "+str(ang))
#     sin_value_in_radian = math . sin(ang) 
#     print("the sin value of the radian angle is = "+str(sin_value_in_radian)+" rad")
#     cos_value_in_radian = math . cos(ang) 
#     print("the cos value of the radian angle is = "+str(cos_value_in_radian)+" rad")
# get_cos_and_sin_in_radian(angle)

import math 
def get_cos_and_sin_in_radian(ang) :
    print("the angle is = "+str(ang)+" rad")
    sin_value_in_radian = math . sin(ang) 
    cos_value_in_radian = math . cos(ang)
    return("the sin value of the radian angle is = "+str(sin_value_in_radian)+" rad , and then the cos value in the radian angle is = "+str(cos_value_in_radian)+" rad")
angle = float(input("please enter the angle is = "))
cos_sin_value = get_cos_and_sin_in_radian(angle)
print(cos_sin_value)