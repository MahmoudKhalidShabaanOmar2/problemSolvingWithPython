# write a python program to get the area of the rectangle by using function methods =>
# width_of_rectangle = float(input("please enter the width of the rectangle is = "))
# length_of_rectangle = float(input("please enter the length of the rectangle is = "))
# def get_area_of_rectangle(wid_of_rect , len_of_rect)  :
#     print("the width of the rectangle is = "+str(wid_of_rect))
#     print("the length of the rectangle is = "+str(len_of_rect))
#     area_of_rectangle = wid_of_rect * len_of_rect 
#     print("the area of the rectangle is = "+str(area_of_rectangle))
# get_area_of_rectangle(width_of_rectangle , length_of_rectangle)

# def get_area_of_rectangle(wid_of_rect , len_of_rect) :
#     print("the width of the rectangle is = "+str(wid_of_rect))
#     print("the length of the rectangle is = "+str(len_of_rect))
#     area_of_rect = len_of_rect * wid_of_rect 
#     return("the area of the rectangle is = "+str(area_of_rect))
# width_of_rectangle = float(input("please enter the width of the rectangle is = "))
# length_of_rectangle = float(input("please enter the length of the rectangle is = "))
# area_of_rectangle = get_area_of_rectangle(width_of_rectangle , length_of_rectangle)
# print(area_of_rectangle)

# width_of_rectangle = float(input("please enter the width of the rectangle is = "))
# length_of_rectangle = float(input("please enter the length of the rectangle is = "))
# def get_area_of_rectangle(wid_of_rect , len_of_rect) :
#     print("the width of the rectangle is = "+str(wid_of_rect))
#     print("the length of the rectangle is = "+str(len_of_rect))
#     if((wid_of_rect > 0) and (len_of_rect > 0)) :
#         area_of_rectangle = wid_of_rect * len_of_rect 
#         print("the area of the rectangle is = "+str(area_of_rectangle)+" , because the width of the rectangle is = "+str(wid_of_rect)+" , and the length of the rectangle is = "+str(len_of_rect))
#     else :
#         print("there is no area of this rectangle , because the width of the rectangle is = "+str(wid_of_rect)+" , and the length of the rectangle is = "+str(len_of_rect))
# get_area_of_rectangle(width_of_rectangle , length_of_rectangle)

def get_area_of_rectangle(wid_of_rect , len_of_rect) :
    print("the width of the rectangle is = "+str(wid_of_rect))
    print("the length of the rectangle is = "+str(len_of_rect))
    if((wid_of_rect > 0) and (len_of_rect > 0)) :
        area_of_rectangle = wid_of_rect * len_of_rect 
        return("the area of the rectangle is = "+str(area_of_rectangle)+" , because the width of the rectangle is = "+str(wid_of_rect))
    else :
        return("there is no area of this rectangle , because the width of the rectangle is = "+str(wid_of_rect)+" , and the length of the rectangle is = "+str(wid_of_rect)) 
length_of_rectangle = float(input("please enter the length of the rectangle is = "))
width_of_rectangle = float(input("please enter the width of the rectangle is = "))
area_of_rect = get_area_of_rectangle(width_of_rectangle , length_of_rectangle)
print(area_of_rect)