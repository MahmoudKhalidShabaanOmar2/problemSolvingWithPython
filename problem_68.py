# write a python program to get name of the day and show "holiday" if user input "sunday" , or "friday" =>
# day_name = input("please enter the name of the day is : ")
# print("the name of the day is : \""+day_name+"\"")
# if((day_name == "Sunday") or (day_name == "Friday")) :
#     print("it is a holiday day")
# elif((day_name == "sunday") or (day_name == "friday")) :
#     print("it is a holiday day")
# elif((day_name == "Fri") or (day_name == "fri")) :
#     print("it is a holiday day")
# elif((day_name == "Sun") or (day_name == "sun")) :
#     print("it is a holiday day")
# else :
#     print("it is a work day")

day_name = input("please enter the name of the day is : ")
print("the name of the day is : \""+day_name+"\"")
if(((day_name == "Friday") or (day_name == "friday") or (day_name == "Fri") or (day_name == "fri")) or ((day_name == "Sunday") or (day_name == "sunday") or (day_name == "Sun") or (day_name == "sun"))) :
    print("it is a holiday day")
else :
    print("it is a work day")