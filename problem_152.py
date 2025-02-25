# write a python program to get two numbers from the user , and then find the cube of the two numbers , and then find the sum of the cube of the two numbers =>
frist_num = int(input("please enter the frist number is = "))
second_num = int(input("please enter the second number is = "))
print("the frist number is = "+str(frist_num))
print("the second number is = "+str(second_num))
addition_of_frist_num_and_second_num = frist_num + second_num 
print("the addition of the two numbers is = "+str(addition_of_frist_num_and_second_num))
cube_of_frist_num = frist_num * frist_num * frist_num 
print("the cube of the frist number is = "+str(cube_of_frist_num))
cube_of_second_num = second_num * second_num * second_num 
print("the cube of the second number is = "+str(cube_of_second_num))
addition_of_cube_of_second_num_and_cube_of_second_num = cube_of_frist_num + cube_of_second_num 
print("the addition of the cube of the two numbers is = "+str(addition_of_cube_of_second_num_and_cube_of_second_num))