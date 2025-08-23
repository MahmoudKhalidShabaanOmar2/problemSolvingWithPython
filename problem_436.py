# write a python program to get the circumference , and area of the circle , and then display the half of the circumference , and area of the circle by using function method =>
import math 
radius_of_circle = float(input("Please Enter The Radius Of The Circle Is = "))
def get_half_of_circumference_area_of_circle(rad_of_circle):
    print("The Radius Of The Circle Is : ",str(rad_of_circle))
    circumference_of_circle = 2 * math.pi * rad_of_circle
    print("The Circumference Of The Circle Is = ",str(circumference_of_circle))
    half_of_circumference_of_circle = 1/2 * circumference_of_circle
    print("The Half Of The Circumference Of The Circle Is = ",str(half_of_circumference_of_circle))
    area_of_circle = 2 * math.pi * rad_of_circle * rad_of_circle 
    print("The Area Of The Circle Is = ",str(area_of_circle))
    half_of_area_of_circle = 1/2 * area_of_circle
    print("The Half Of The Area Of The Circle Is = ",str(half_of_area_of_circle))
get_half_of_circumference_area_of_circle(radius_of_circle)
    