# write a python program to get the number from the user to display the value of the sin , and cos value of the next number , and previous number =>
import math
number = int(input("Please Enter The Number Is = "))
print("The Number Is = ",str(number))
sin_of_number = math.sin(number)
print("The Sin Of The Number Is = ",str(sin_of_number))
cos_of_number = math.cos(number)
print("The Cos Of The Number Is = ",str(cos_of_number))
next_number = number + 1
print("The Next Number Is = ",str(next_number))
sin_of_next_number = math.sin(next_number)
print("The Sin Of The Next Number Is = ",str(sin_of_next_number))
cos_of_next_number = math.cos(next_number)
print("The Cos Of The Next Number Is = ",str(cos_of_next_number))
previous_number = number - 1
print("The Previous Number Is = ",str(previous_number))
sin_of_previous_number = math.sin(previous_number)
print("The Sin Of The Previous Number Is = ",str(sin_of_previous_number))
cos_of_previous_number = math.cos(previous_number)
print("The Cos Of The Previous Number Is = ",str(cos_of_previous_number))