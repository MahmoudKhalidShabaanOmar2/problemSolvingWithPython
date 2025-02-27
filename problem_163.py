# write a python program to get area of the rectangle by using different function methods =>
# rectangle_length = float(input("please enter the length of the rectangle is = "))
# rectangle_width = float(input("please enter the width of the rectangle is = "))
# def get_area_of_rectangle(wid_of_rect , len_of_rect) :
#     print("the length of the rectangle is = "+str(wid_of_rect))
#     print("the width of the rectangle is = "+str(len_of_rect))
#     area_of_rectangle = wid_of_rect * len_of_rect
#     print("the area of the rectangle is = "+str(area_of_rectangle))
# get_area_of_rectangle(rectangle_width , rectangle_length)

# def get_area_of_rectangle(wid_of_rect , len_of_rect) :
#     print("the width of the rectangle is = "+str(wid_of_rect))
#     print("the length of the rectangle is = "+str(len_of_rect))
#     area_of_rectangle = wid_of_rect * len_of_rect 
#     return("the area of the rectangle is = "+str(area_of_rectangle))
# width_of_rectangle = float(input("please enter the width of the rectangle is = "))
# length_of_rectangle = float(input("please enter the length of the rectangle is = "))
# rectangle_area = get_area_of_rectangle(width_of_rectangle , length_of_rectangle)
# print(rectangle_area)

# width_of_rectangle = float(input("please enter the width of the rectangle is = "))
# length_of_rectangle = float(input("please enter the length of the rectangle is = "))
# def get_area_of_rectangle(wid_of_rect , len_of_rect) :
#     print("the width of the rectangle is = "+str(wid_of_rect)) 
#     print("the length of the rectangle is = "+str(len_of_rect))
#     if((wid_of_rect > 0) and (len_of_rect > 0)) :
#         rectangle_area = wid_of_rect * len_of_rect 
#         print("the area of the rectangle is = "+str(rectangle_area))
#     else :
#         print("there is no area of the rectangle")
# get_area_of_rectangle(width_of_rectangle , length_of_rectangle)

def get_area_of_rectangle(wid_of_rect , len_of_rect) :
    print("the length of the rectangle is = "+str(len_of_rect))
    print("the width of the rectangle is = "+str(wid_of_rect))
    if((wid_of_rect > 0) and (len_of_rect > 0)) :
        area_of_rectangle = wid_of_rect * len_of_rect 
        return("the area of the rectangle is = "+str(area_of_rectangle))
    else :
        return("there is no area of the rectangle")
width_of_rectangle = float(input("please enter the width of the rectangle is = "))
length_of_rectangle = float(input("please enter the length of the rectangle is = "))
rectangle_area = get_area_of_rectangle(width_of_rectangle , length_of_rectangle)
print(rectangle_area)