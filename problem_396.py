# write  a python program to calculate the area of the circle by using function method =>
# import math 
# radius_of_circle = float(input("Please Enter The Radius Of The Circle Is = "))
# def get_area_of_circle(rad_of_circle) :
#     print("The Radius Of The Circle Is = ",str(rad_of_circle))
#     # area_of_circle = math.pi * rad_of_circle * rad_of_circle 
#     # area_of_circle = math.pi * pow(rad_of_circle , 2)
#     area_of_circle = math.pi * rad_of_circle ** 2 
#     print("The Radius Of The Circle Is = ",str(area_of_circle))
# get_area_of_circle(radius_of_circle)

import math 
def get_area_of_circle(rad_of_circle) :
    print("The Radius Of The Circle Is = ",str(rad_of_circle))
    # area_of_circle = math.pi * rad_of_circle * rad_of_circle 
    # area_of_circle = math.pi * rad_of_circle ** 2 
    area_of_circle = math.pi * math.pow(rad_of_circle , 2)
    return("The Area Of The Circle Is = "+str(area_of_circle))
radius_of_circle = float(input("Please Enter The Radius Of The Circle Is = "))
displaying_area_of_circle = get_area_of_circle(radius_of_circle)
print(displaying_area_of_circle)