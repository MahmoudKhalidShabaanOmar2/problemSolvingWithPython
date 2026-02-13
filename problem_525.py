# write a returned function to return the circumference , and area of the function by using python language =>
import math 
def get_circumference_area_of_circle(rad_of_circle):
    print("The Radius Of The Circle Is : ",str(rad_of_circle))
    circumference_of_circle = 2 * math.pi * rad_of_circle 
    # area_of_circle = 2 * math.pi * rad_of_circle * rad_of_circle 
    # area_of_circle = 2 * math.pi * math.pow(rad_of_circle , 2)
    area_of_circle = 2 * math.pi * rad_of_circle ** 2
    return ("The Circumference Of The Circle Is = "+str(circumference_of_circle)+" , And The Area Of The Circle Is = "+str(area_of_circle))
radius_of_circle = float(input("Please Enter The Radius Circle Is = "))
circumference_and_area_of_circle = get_circumference_area_of_circle(radius_of_circle)
print(circumference_and_area_of_circle)