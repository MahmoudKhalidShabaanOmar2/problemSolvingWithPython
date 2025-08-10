# write a python program to get number from the user , and then get the cube of the next number , and previous number from the number =>
import math 
number = int(input("Please Enter The Number Is = "))
print("The Number Is = ",str(number))
# cube_of_number = number * number * number
# cube_of_number = math.pow(number , 2)
cube_of_number = number ** 3
print("The Cube Of The Number Is = ",str(cube_of_number))
next_number = number + 1
print("The Next Number Is = ",str(next_number))
# cube_of_next_number = next_number * next_number * next_number
# cube_of_next_number = math.pow(next_number , 3)
cube_of_next_number = next_number ** 3
print("The Cube Of The Next Number Is = ",str(cube_of_next_number))
previous_number = number - 1 
print("The Previous Number Is = ",str(previous_number))
# cube_of_previous_number = previous_number * previous_number * previous_number
# cube_of_previous_number = math.pow(previous_number , 3)
cube_of_previous_number = previous_number ** 3
print("The Cube Of The Previous Number Is = ",str(cube_of_previous_number))