# write a python program to get the number from the user , and then get the flooring of the number by using function method =>
# import math 
# number = float(input("Please Enter The Number Is = "))
# def getting_flooring_of_number(num) :
#     print("The Number Is = ",str(num))
#     flooring_of_number = math.floor(num)
#     print("The Flooring Of The Number Is = ",str(flooring_of_number))
# getting_flooring_of_number(number)

import math 
def getting_flooring_of_number(num) :
    print("The Number Is = ",str(num))
    flooring_of_number = math.floor(num)
    print("The Flooring Of The Number Is : ")
    return flooring_of_number
number = float(input("Please Enter The Number Is = "))
displaying_flooring_of_number = getting_flooring_of_number(number)
print(displaying_flooring_of_number)