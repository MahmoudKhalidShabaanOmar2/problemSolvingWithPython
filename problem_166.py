# write a python program to get the area of the traingle , and then get number from the user , and then get the cube of the number , and also display the sum of the area of the traingle , and square of the number =>
# base_of_traingle = float(input("please enter the base of the traingle is = "))
# height_of_traingle = float(input("please enter the height of the traingle is = "))
# print("the base of the traingle is = "+str(base_of_traingle))
# print("the height of the traingle is = "+str(height_of_traingle))
# area_of_traingle = 1/2 * (base_of_traingle * height_of_traingle)
# print("the area of the traingle is = "+str(area_of_traingle))
# num = int(input("please enter the number is = "))
# print("the number is = "+str(num))
# # cube_of_num = num * num * num 
# # cube_of_num = num ** 3
# cube_of_num = pow(num , 3)
# print("the cube of the number is = "+str(cube_of_num))
# sum_of_area_of_traingle_and_cube_of_num = area_of_traingle + cube_of_num 
# print("the sum of the area of the traingle , and cube of the number is = "+str(sum_of_area_of_traingle_and_cube_of_num))

base_of_traingle = float(input("please enter the base of the traingle is = "))
height_of_traingle = float(input("please enter the height of the traingle is = "))
number = int(input("please enter the number is = "))
if((base_of_traingle > 0) and (height_of_traingle > 0)) :
    area_of_traingle = 1/2 * (base_of_traingle * height_of_traingle)
    print("the area of the traingle is = "+str(area_of_traingle))
else :
    print("there is no area of the rectangle")
print("the number is = "+str(number))
if(number > 0) :
    cube_of_num = number * number * number 
    print("the cube of the number is = "+str(cube_of_num))
else :
    print("there is no cube of the number")
sum_of_traingle_area_and_cube_of_num = area_of_traingle + cube_of_num 
print("the sum of the area of the traingle , and the cube of the number is = "+str(sum_of_traingle_area_and_cube_of_num))