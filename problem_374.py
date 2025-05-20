# write a python to get the number from the user , and then getting the celling of the number by using function methods =>
# import math 
# number = float(input("Please Enter The Number Is = "))
# def get_ceiling_of_number(num) :
#     print("The Number Is = ",str(num))
#     ceiling_of_number = math.ceil(num)
#     print("The Ceiling Of The Number Is = ",str(ceiling_of_number))
# get_ceiling_of_number(number)

import math 
def getting_ceiling_of_number(num) :
    print("The Number Is = ",str(num))
    ceiling_of_number = math.ceil(num)
    print("The Ceiling Of The Number Is = ")
    return ceiling_of_number
number = float(input("Please Enter The Number Is = "))
displaying_ceiling_of_number = getting_ceiling_of_number(number)
print(displaying_ceiling_of_number)