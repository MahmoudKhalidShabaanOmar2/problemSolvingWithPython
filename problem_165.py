# write a python program to get area of the rectangle , and then get number from the user , and find the square of the number , and then display the sum of the area of the rectangle , and square of the number by using different functions methods =>
# width_of_rectangle = float(input("please enter the width of the rectangle is = "))
# length_of_rectangle = float(input("please enter the length of the rectangle is = "))
# number = int(input("please enter the number is = "))
# def get_rectangle_area_and_square_of_number(wid_of_rect , len_of_rect , num) :
#     print("the length of the rectangle is = "+str(len_of_rect))
#     print("the width of the rectangle is = "+str(wid_of_rect))
#     area_of_rectangle = len_of_rect * wid_of_rect 
#     print("the area of the rectangle is = "+str(area_of_rectangle))
#     print("the number is = "+str(num))
#     # square_of_number = num * num 
#     # square_of_number = num ** 2
#     square_of_number = pow(num , 2)
#     print("the square of the number is = "+str(square_of_number)+" , because your entered number is = "+str(num))
#     sum_of_rectangle_area_and_square_of_num = area_of_rectangle + square_of_number 
#     print("the sum of the area of the rectangle , and square of the number is = "+str(sum_of_rectangle_area_and_square_of_num))
# get_rectangle_area_and_square_of_number(width_of_rectangle , length_of_rectangle , number)

# def get_rectangle_area_and_square_of_number(wid_of_rect , len_of_rect , num) :
#     print("the width of the rectangle is = "+str(wid_of_rect))
#     print("the length of the rectangle is = "+str(len_of_rect))
#     if((len_of_rect > 0) and (wid_of_rect)) :
#         area_of_rectangle = len_of_rect * wid_of_rect 
#         print ("the area of the rectangle is = "+str(area_of_rectangle))
#     else :
#         print ("there is no area of the rectangle")
#     print("the number is = "+str(num))    
#     if(num > 0) :
#         # square_of_number = num * num 
#         # square_of_number = pow(num , 2)
#         square_of_number = num ** 2
#         print("the square of the number is = "+str(square_of_number)+" , because your entered number is = "+str(num))
#     else : 
#         print("there is no square of this number")
#     sum_of_area_of_rectangle_and_square_of_number = area_of_rectangle + square_of_number
#     print("the sum of the area of the rectanlge , and square of the number is = "+str(sum_of_area_of_rectangle_and_square_of_number))
#     return("")
# width_of_rectangle = float(input("please enter the width of the rectangle is = "))
# length_of_rectangle = float(input("please enter the length of the rectangle is = "))
# number = int(input("please enter the number is = "))
# rectangle_area_and_square_of_number = get_rectangle_area_and_square_of_number(width_of_rectangle , length_of_rectangle , number)
# print(rectangle_area_and_square_of_number)

width_of_rectangle = float(input("please enter the width of the rectangle is = "))
length_of_rectangle = float(input("please enter the length of the rectangle is = "))
number = int(input("please enter the number is = "))
def get_rectangle_area_and_square_of_number(wid_of_rect , len_of_rect , num) :
    print("the width of the rectangle is = "+str(wid_of_rect))
    print("the length of the rectangle is = "+str(len_of_rect))
    if((wid_of_rect > 0) and (len_of_rect > 0)) :
        area_of_rectangle = wid_of_rect * len_of_rect 
        print("the area of the rectangle is = "+str(area_of_rectangle))
    else : 
        print("there is no area of the rectangle")
    print("the number is = "+str(num))
    if(num > 0) :
        # square_of_num = num * num 
        # square_of_num = num ** 2
        square_of_num = pow(num , 2)
        print("the square of the number is = "+str(square_of_num))
    else :
        print("there is no square of the number")
    sum_of_rectangle_area_and_square_of_number = area_of_rectangle + square_of_num 
    print("the sum of the area of the traingle , and square of the number is = "+str(sum_of_rectangle_area_and_square_of_number))
get_rectangle_area_and_square_of_number(width_of_rectangle , length_of_rectangle , number)