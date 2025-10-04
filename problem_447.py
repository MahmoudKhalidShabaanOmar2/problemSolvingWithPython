# write a python program to get the area , and circumference of the circle , half the answer of the circumference , and area of the circle then add both results , and finally displaying for the user =>
import math 
radius_of_circle = float(input("Please Enter The Raadius Of The Circle Is = "))
print("THe Radius Of The Circle Is = ",str(radius_of_circle))
area_of_circle = math.pi * radius_of_circle * radius_of_circle

print("The Area Of The Circle Is = ",str(area_of_circle))
half_of_area_of_circle = 1/2 * area_of_circle 
print("The Half Of The Area Of The Circle Is = ",str(half_of_area_of_circle))
circumference_of_circle = 2 * math.pi * radius_of_circle 
print("The Circumference Of The Circle Is = ",str(circumference_of_circle))
half_of_circumference_of_circle = 1/2 * circumference_of_circle
print("The Half Of The Circumference Of The Circle Is = ",str(half_of_circumference_of_circle))
sum_of_half_of_area_circumference_of_circle = half_of_area_of_circle + half_of_circumference_of_circle 
print("The Sum Of The Half Of The Area Of The Circle , And The Half Of The Circumference Of The Circle Is = ",str(sum_of_half_of_area_circumference_of_circle))