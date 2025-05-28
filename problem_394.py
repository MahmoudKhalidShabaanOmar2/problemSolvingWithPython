# write a python program to calculate the circumference of the circle by using function method =>
# import math 
# radius_of_circle = float(input("Please Enter The Radius Of The Circle Is = "))
# def get_circumference_of_circle(rad_of_circle) :
#     print("The Radius Of The Circle Is = ",str(rad_of_circle))
#     circumference_of_circle = 2 * math.pi * rad_of_circle 
#     print("The Circumference Of The Circle Is = ",str(circumference_of_circle))
# get_circumference_of_circle(radius_of_circle)

import math 
def get_circumference_of_circle(rad_of_circle) :
    print("The Radius Of The Circle Is = ",str(rad_of_circle))
    circumference_of_circle = 2 * math.pi * rad_of_circle 
    return("The Circumference Of The Circle Is = "+str(circumference_of_circle))
radius_of_circle = float(input("Please Enter The Radius Of The Circle Is = "))    
displaying_circumference_of_circle = get_circumference_of_circle(radius_of_circle)
print(displaying_circumference_of_circle)