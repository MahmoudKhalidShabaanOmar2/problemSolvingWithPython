# write a python program to calculate the area of the circle =>
import math 
radius_of_circle = float(input("please enter the radius of the circle is = "))
print("the radius of the circle is = "+str(radius_of_circle))
# area_of_circle = math.pi * radius_of_circle * radius_of_circle 
# area_of_circle = math.pi * (radius_of_circle ** 2) 
area_of_circle = math.pi * (pow(radius_of_circle , 2))
print("the area of the circle is = "+str(area_of_circle)+" , because the radius of the circle is = "+str(radius_of_circle))