# write a python program to get degree angle from the user to radian angle by using different functions methods =>
import math 
# degree_angle = float(input("please enter the radian angle is = "))
# def get_radian_angle(deg_angle) :
#     print("the degree angle is = "+str(deg_angle)+"deg")
#     radian_angle = math . radians(deg_angle)
#     print("the radian angle is = "+str(radian_angle)+"rad")
# get_radian_angle(degree_angle)

def get_radian_angle(deg_angle) :
    print("the degree angle is = "+str(deg_angle)+"deg")
    radian_angle = math . radians(deg_angle)
    return("the radian angle is = "+str(radian_angle)+"rad")
degree_angle = float(input("please enter the degree angle is = "))
radians = get_radian_angle(degree_angle)
print(radians)