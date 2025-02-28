# write a python program to get the area of the traingle =>
# base_of_traingle = float(input("please enter the base of the traingle is = "))
# height_of_traingle = float(input("please enter the height of the traingle is = "))
# print("the base of the traingle is = "+str(base_of_traingle))
# print("the height of the traingle is = "+str(height_of_traingle))
# area_of_traingle = 1/2 * (base_of_traingle * height_of_traingle)
# print("the area of the traingle is = "+str(area_of_traingle))

base_of_traingle = float(input("please enter the base of the traingle is = "))
height_of_traingle = float(input("please enter the height of the traingle is = "))
print("the base of the traingle is = "+str(base_of_traingle))
print("the height of the traingle is = "+str(height_of_traingle))
if((base_of_traingle > 0) and (height_of_traingle > 0)) :
    area_of_traingle = 1/2 * (base_of_traingle * height_of_traingle)
    print("the area of the traingle is = "+str(area_of_traingle))
else :
    print("there is no area of the traingle")