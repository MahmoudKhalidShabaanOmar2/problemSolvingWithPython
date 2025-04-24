# write a python program to get floor , and ceiling of the number =>
import math 
number = float(input("Please Enter The Number Is = "))
print("The Number Is = ",number)
ceilingOfNumber = math . ceil(number)
print("The Ceiling Of The Number Is = ",str(ceilingOfNumber)," , Because Your Entered Number Is = ",number)
flooringOfNumber = math . floor(number)
print("The Flooring Of The Number Is = ",str(flooringOfNumber)," , Because Your Entered Number Is = ",number)