# write a python program to calculate the circumference , and area of the circle by using function method =>
import math 
radius_of_circle = float(input("Please Enter The Radius Of The Circle Is = "))
def get_circumference_area_of_circle(rad_of_circle) :
    print("The Radius Of The Circle Is = ",rad_of_circle)
    circumference_of_circle = math.pi * 2 * rad_of_circle 
    print("The Circumference Of The Circle Is = ",str(circumference_of_circle))
    # area_of_circle = math.pi * rad_of_circle * rad_of_circle 
    # area_of_circle = math.pi * pow(rad_of_circle , 2)
    area_of_circle = math.pi * rad_of_circle ** 2
    print("The Area Of The Circle Is = ",str(area_of_circle))
get_circumference_area_of_circle(radius_of_circle)