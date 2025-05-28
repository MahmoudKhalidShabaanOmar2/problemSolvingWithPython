# write a python program to calculate the circumference , and area of the circle =>
import math 
radius_of_circle = float(input("Please Enter The Radius Of The Circle Is = "))
print("The Radius Of The Circle Is = ",str(radius_of_circle))
# area_of_circle = math.pi * radius_of_circle * radius_of_circle 
# area_of_circle = math.pi * pow(radius_of_circle , 2)
area_of_circle = math.pi * radius_of_circle ** 2 
print("The Area Of The Circle Is = ",str(area_of_circle))
circumference_of_circle = 2 * math.pi * radius_of_circle 
print("The Circumference Of The Circle Is = ",str(circumference_of_circle))