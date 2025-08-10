# write a python program python program to get the number from the user , and then get the square of the previous number , and next number =>
import math 
number = int(input("Please Enter The Number Is = "))
print("The Number Is = ",str(number))
# square_of_number = number * number
# square_of_number = number ** 2
square_of_number = math.pow(number , 2)
print("The Square Of The Number Is = ",str(square_of_number))
previous_number = number - 1
print("The Previous Number Is = ",str(previous_number))
# square_of_previous_number = previous_number * previous_number
# square_of_previous_number = previous_number ** 2
square_of_previous_number = math.pow(previous_number , 2)
print("The Square Of The Previous Number Is = ",str(square_of_previous_number))
next_number = number + 1
print("The Next Number Is = ",str(next_number))
# square_of_next_number = next_number * next_number
# square_of_next_number = next_number ** 2
square_of_next_number = math.pow(next_number , 2)
print("The Square Of The Next Number Is = ",str(square_of_next_number))