# write a python program to get angle from the user , and then find it's cos , and sin value in radian =>
import math 
angle = float(input("please enter the angle is = "))
print("the angle is = "+str(angle)+" radians")
sin_value_of_radian_angle = math . sin(angle)
print("the sin value of the radian angle is = "+str(sin_value_of_radian_angle)+" rad")
cos_value_of_radian_angle = math . cos(angle) 
print("the cos value of the radian angle is = "+str(cos_value_of_radian_angle)+" rad")