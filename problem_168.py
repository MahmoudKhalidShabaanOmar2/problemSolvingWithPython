# write a python program to get area of the traingle by using different functions methods =>
# base_of_traingle = float(input("please enter the base of the traingle is = "))
# height_of_traingle = float(input("please enter the height of the traingle is = "))
# def get_area_of_traingle(train_base , train_high) :
#     print("the base of the traingle is = "+str(train_base))
#     print("the height of the traingle is = "+str(train_high))
#     area_of_traingle = 1/2 * (train_base * train_high)
#     print("the area of the traingle is = "+str(area_of_traingle))
# get_area_of_traingle(base_of_traingle , height_of_traingle)

# def get_area_of_traingle(train_base , train_high) :
#     print("the base of the traingle is = "+str(train_base))
#     print("the height of the traingle is = "+str(train_high))
#     area_of_traingle = 1/2 * (train_base * train_high)
#     return("the area of the traingle is = "+str(area_of_traingle))
# base_of_traingle = float(input("please enter the base of the traingle is = "))
# height_of_traingle = float(input("please enter the height of the traingle is = "))
# traingle_area = get_area_of_traingle(base_of_traingle , height_of_traingle)
# print(traingle_area)

# base_of_traingle = float(input("please enter the base of the traingle is = "))
# height_of_traingle = float(input("please enter the height of the traingle is = "))
# def get_area_of_traingle(train_base , train_high) :
#     print("the base of the traingle is = "+str(train_base))
#     print("the height of the traingle is = "+str(train_high))
#     if((train_base > 0) and (train_high > 0)) :
#         area_of_traingle = 1/2 * (train_base * train_high)
#         print("the area of the traingle is = "+str(area_of_traingle))
#     else :
#         print("there is no area of the traingle")
# get_area_of_traingle(base_of_traingle , height_of_traingle)

# def get_area_of_traingle(train_base , train_high) :
#     print("the base of the traingle is = "+str(train_base))
#     print("the height of the traingle is = "+str(train_high))
#     if((train_base > 0) and (train_high > 0)) :
#         area_of_traingle = 1/2 * (train_base * train_high) 
#         return ("the area of the traingle is = "+str(area_of_traingle))
#     else :
#         return("there is no area of the traingle")
# base_of_traingle = float(input("please enter the base of the traingle is = "))
# height_of_traingle = float(input("please enter the height of the traingle is = "))
# traingle_area = get_area_of_traingle(base_of_traingle , height_of_traingle)
# print(traingle_area)

def get_area_of_traingle(train_base , train_high) :
    print("the base of the traingle is = "+str(train_base))
    print("the height of the traingle is = "+str(train_high))
    area_of_traingle = 1/2 * (train_base * train_high)
    return("the area of the traingle is = "+str(area_of_traingle))
base_of_traingle = float(input("please enter the base of the traingle is = "))
height_of_traingle = float(input("please enter the height of the traingle is = "))
traingle_area = get_area_of_traingle(base_of_traingle , height_of_traingle)
print(traingle_area)