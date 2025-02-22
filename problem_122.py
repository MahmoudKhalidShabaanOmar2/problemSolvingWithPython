# write a python program to get radian angle from the user and then converted to degree angle by using different function methods =>
import math 
# radian_angle = float(input("please enter the radian angle is = "))
# def get_degree_angle(rad_angle) :
#     print("the radian angle is = "+str(rad_angle)+"rad")
#     degree_angle = math . degrees(rad_angle)
#     print("the degree angle is = "+str(degree_angle)+"deg")
# get_degree_angle(radian_angle)

def get_degree_angle(rad_angle) :
    print("the radian angle is = "+str(rad_angle)+"rad")
    degree_angle = math . degrees(rad_angle)
    return("the degree angle is = "+str(degree_angle)+"deg")
radian_angle = float(input("please enter the radian angle is = "))
deg_angle = get_degree_angle(radian_angle)
print(deg_angle)