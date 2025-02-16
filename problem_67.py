# write a python program to get name of the day and show "holiday" if user input "sunday" =>
# day_name = input("please enter the name of the day is : ")
# print("the name of the day is : \""+day_name+"\"")
# if((day_name == "sunday")) :
#     print("it is a holiday day")
# elif((day_name == "Sunday")) :
#     print("it is a holiday day") 
# elif((day_name == "sun")) :
#     print("it is a holiday day")
# elif((day_name == "Sun")) :
#     print("it is a holiday day")
# else :
#     print("it is a work day")

day_name = input("please enter the name of the day is : ")
print("the name of the day is : \""+day_name+"\"")
if((day_name == "Sunday") or (day_name == "sunday") or (day_name == "Sun") or (day_name == "sun")) :
    print("it is a holiday day")
else : 
    print("it is not a work day")