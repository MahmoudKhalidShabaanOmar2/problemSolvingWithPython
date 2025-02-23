# write a python program to get angle from the user , and find it's sin , and cos value in radian , and then converted their results into degree unit =>
import math 
angle = float(input("please enter the angle is = "))
print("the angle is = "+str(angle)+" rad")
cos_value_in_radian = math . cos(angle)
print("the cos value in the radian angle is = "+str(cos_value_in_radian)+" rad")
cos_value_in_degree = math . degrees(cos_value_in_radian)
print("the cos value in the degree angle is = "+str(cos_value_in_degree)+" deg")
sin_value_in_radian = math . sin(angle)
print("the sin value in the radian angle is = "+str(sin_value_in_radian)+" rad")
sin_value_in_degree = math . degrees(sin_value_in_radian)
print("the sin value in the degree angle is = "+str(sin_value_in_degree)+" deg")
