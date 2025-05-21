# write a python program to get number from the user , and then get the flooring , and ceiling of the number by using function method =>
# import math 
# number = float(input("Please Enter The Floating Number Is = "))
# def getting_flooring_ceiling_of_number(num) :
#     print("The Floating Number Is = ",num)
#     flooring_of_number = math . floor(num)
#     print("The Flooring Of The Number Is = ",str(flooring_of_number))
#     ceiling_of_number = math . ceil(num)
#     print("The Ceiling Of The Number Is = ",str(ceiling_of_number))
# getting_flooring_ceiling_of_number(number)

import math 
def get_flooring_ceiling_of_number(num) :
    print("The Floating Number Is = ",str(num))
    flooring_of_number = math.floor(num)
    ceiling_of_number = math.ceil(num)
    return"The Flooring Of The Number Is = " , str(flooring_of_number) , "The Ceiling Of The Number Is = ",str(ceiling_of_number)
number = float(input("Please Enter The Floating Number Is = "))
displaying_flooring_ceiling_of_number = get_flooring_ceiling_of_number(number)
print(displaying_flooring_ceiling_of_number)