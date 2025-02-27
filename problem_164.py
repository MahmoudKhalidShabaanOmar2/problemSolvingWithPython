# write a python program to get the area of the rectangle , and then get the number from the user , and find the square of this number , and then display the sum of the area of the traingle , and square of number => 
# width_of_rectangle = float(input("please enter the width of the rectangle is = "))
# length_of_rectangle = float(input("please enter the length of the rectangle is = "))
# print("the width of the rectangle is = "+str(width_of_rectangle))
# print("the length of the rectangle is = "+str(length_of_rectangle))
# area_of_rectangle = width_of_rectangle * length_of_rectangle 
# print("the area of the rectangle is = "+str(area_of_rectangle))
# num = int(input("please enter the number is = "))
# print("the number is = "+str(num))
# # square_of_number = num * num 
# # square_of_number = num ** 2
# square_of_number = pow(num , 2)
# print("the square of the number is = "+str(square_of_number))
# sum_of_rectangle_area_and_square_of_num = area_of_rectangle + square_of_number 
# print("the sum of the area of the traingle , and square of the number is = "+str(sum_of_rectangle_area_and_square_of_num))

width_of_rectangle = float(input("please enter the width of the rectangle is = "))
length_of_rectangle = float(input("please enter the length of the rectangle is = "))
number = int(input("please enter the number is = "))
print("the width of the rectangle is = "+str(width_of_rectangle))
print("the length of the rectangle is = "+str(length_of_rectangle))
if((width_of_rectangle > 0) and (length_of_rectangle > 0)) :
    area_of_rectangle = width_of_rectangle * length_of_rectangle 
    print("the area of the rectangle is = "+str(area_of_rectangle))
else :
    print("there is no area of the rectangle")
print("the number is = "+str(number))
if(number > 0) :
    # square_of_number = number * number 
    # square_of_number = number ** 2
    square_of_number = pow(number , 2)
    print("the square of the number is = "+str(square_of_number))
else :
    print("there is no square of the number")
sum_of_rectangle_area_and_square_of_num = area_of_rectangle + square_of_number 
print("the sum of the rectangle area , and square of the number is = "+str(sum_of_rectangle_area_and_square_of_num))