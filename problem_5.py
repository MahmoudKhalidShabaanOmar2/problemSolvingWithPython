# write a python program to get area of the rectangle =>
# width_of_rectangle = float(input("please enter the width of the rectangle is = "))
# length_of_rectangle = float(input("please enter the length of the rectsngle is = "))
# print("the width of the rectangle is = "+str(width_of_rectangle))
# print("the length of the rectangle is = "+str(width_of_rectangle))
# area_of_rectangle = width_of_rectangle * length_of_rectangle 
# print("the area of the rectangle is = "+str(area_of_rectangle)+" , because the width of the rectangle is = "+str(width_of_rectangle)+" , and the length of the rectangle is = "+str(length_of_rectangle))

width_of_rectangle = float(input("please enter the width of the rectangle is = "))
length_of_rectangle = float(input("please enter the length of the rectangle is = "))
print("the width of the rectangle is = "+str(width_of_rectangle))
print("the length of the rectangle is = "+str(length_of_rectangle))
if((width_of_rectangle > 0) and (length_of_rectangle > 0)) :
    area_of_rectangle = width_of_rectangle * length_of_rectangle 
    print("the area of the rectangle is = "+str(area_of_rectangle)+" , because the width of the rectangle is = "+str(width_of_rectangle)+" , and the length of the rectangle is = "+str(length_of_rectangle))
else :
    print("there is no area of the rectangle , because the width of the rectangle is = "+str(width_of_rectangle)+" , and the length of the rectangle is = "+str(length_of_rectangle))